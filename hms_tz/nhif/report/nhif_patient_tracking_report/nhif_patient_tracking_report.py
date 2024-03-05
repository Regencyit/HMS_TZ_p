# Copyright (c) 2022, Aakvatech and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    if not filters:
        return

    columns = get_columns()
    records = get_data(filters)

    data = sorted(
        records,
        key=lambda x: (x["appointment_date"], x["patient"], x["authorization_number"]),
    )

    return columns, data


def get_columns():
    return [
        {
            "fieldname": "appointment_date",
            "label": _("Appointment Date"),
            "fieldtype": "Date",
        },
        {"fieldname": "patient", "label": _("Patient"), "fieldtype": "Data"},
        {"fieldname": "patient_name", "label": _("Patient Name"), "fieldtype": "Data"},
        {
            "fieldname": "appointment_no",
            "label": _("AppointmentNo"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "authorization_number",
            "label": _("AuthorizationNo"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "appointment_status",
            "label": _("Appointment Status"),
            "fieldtype": "Data",
        },
        {"fieldname": "encounter", "label": _("Last Encounter"), "fieldtype": "Data"},
        {
            "fieldname": "encounter_status",
            "label": _("Status of Last Encounter"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "inpatient_status",
            "label": _("Inpatient Status"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "nhif_claim_no",
            "label": _("NHIF Patient Claim"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "signature",
            "label": _("Signature Captured"),
            "fieldtype": "Data",
        },
    ]


def get_data(filters):
    nhif_records = []
    nhif_appointments = []
    appointment_nos, patient_details = get_encounter_details(filters)

    nhif_claims = frappe.get_all(
        "NHIF Patient Claim",
        filters={
            "patient_appointment": ["in", appointment_nos],
            "company": filters.company,
        },
        fields=["patient_appointment", "patient", "name", "patient_signature"],
        order_by="attendance_date",
    )
    if not nhif_claims:
        return patient_details

    for d in patient_details:
        for claim in nhif_claims:
            if d["appointment_no"] == claim["patient_appointment"]:
                nhif_appointments.append(d["appointment_no"])

                if claim["patient_signature"]:
                    signature = "Yes"
                else:
                    signature = ""

                nhif_records.append(
                    {
                        "appointment_date": d["appointment_date"],
                        "patient": d["patient"],
                        "patient_name": d["patient_name"],
                        "appointment_no": d["appointment_no"],
                        "authorization_number": d["authorization_number"],
                        "appointment_status": d["appointment_status"],
                        "encounter": d["encounter"] or "",
                        "encounter_status": d["encounter_status"] or "",
                        "inpatient_status": d["ipd_status"] or "",
                        "nhif_claim_no": claim["name"] or "",
                        "signature": signature,
                    }
                )

        if d["appointment_no"] not in nhif_appointments:
            nhif_records.append(
                {
                    "appointment_date": d["appointment_date"],
                    "patient": d["patient"],
                    "patient_name": d["patient_name"],
                    "appointment_no": d["appointment_no"],
                    "authorization_number": d["authorization_number"],
                    "appointment_status": d["appointment_status"],
                    "encounter": d["encounter"] or "",
                    "encounter_status": d["encounter_status"] or "",
                    "inpatient_status": d["ipd_status"] or "",
                    "nhif_claim_no": "",
                    "signature": "",
                }
            )

    return nhif_records


def get_encounter_details(filters):
    appointment_list = []
    appointment_nos, appointments = get_appointment_details(filters)

    encounters = frappe.get_all(
        "Patient Encounter",
        filters={
            "appointment": ["in", appointment_nos],
            "company": filters.company,
            "duplicated": 0,
            "insurance_company": "NHIF",
        },
        fields=["appointment", "patient", "name", "docstatus"],
        order_by="encounter_date",
    )
    if not encounters:
        return appointment_nos, appointments

    encounter_details = []
    for appointment in appointments:
        for enc in encounters:
            if appointment["appointment_no"] == enc.appointment:
                appointment_list.append(appointment["appointment_no"])

                status = ""
                if enc.docstatus == 0:
                    status += "Draft"
                if enc.docstatus == 1:
                    status += "Submitted"
                if enc.docstatus == 2:
                    status += "Cancelled"

                appointment.update({"encounter": enc.name, "encounter_status": status})
                encounter_details.append(appointment)

        if appointment["appointment_no"] not in appointment_list:
            appointment.update({"encounter": "", "encounter_status": ""})
            encounter_details.append(appointment)

    return appointment_nos, encounter_details


def get_appointment_details(filters):
    name_list, entries = [], []
    appointment_list = []
    conditions = get_conditions(filters)

    appointments = frappe.get_all(
        "Patient Appointment",
        filters=conditions,
        fields=[
            "name",
            "patient",
            "patient_name",
            "appointment_date",
            "status",
            "authorization_number",
        ],
        order_by="appointment_date",
    )
    if not appointments:
        frappe.throw(
            "No Appointment(s) Found for the filters: #{0}, #{1} and #{2}".format(
                frappe.bold(filters.date),
                frappe.bold(filters.company),
                frappe.bold(filters.status),
            )
        )

    for pa in appointments:
        name_list.append(pa["name"])
        appointment_list.append(
            {
                "appointment_date": pa["appointment_date"],
                "patient": pa["patient"],
                "patient_name": pa["patient_name"],
                "appointment_no": pa["name"],
                "authorization_number": pa["authorization_number"],
                "appointment_status": pa["status"],
            }
        )

    inpatient_records = frappe.get_all(
        "Inpatient Record",
        filters={"patient_appointment": ["in", name_list], "insurance_company": "NHIF"},
        fields=["status", "patient_appointment"],
    )

    appointment_details = []
    for appointment in appointment_list:
        if inpatient_records:
            for record in inpatient_records:
                if appointment["appointment_no"] == record.patient_appointment:
                    entries.append(appointment["appointment_no"])
                    appointment["ipd_status"] = record.status
                    appointment_details.append(appointment)

        if appointment["appointment_no"] not in entries:
            appointment["ipd_status"] = ""
            appointment_details.append(appointment)

    return name_list, appointment_details


def get_conditions(filters):
    if filters:
        conditions = []
        if filters.from_date and filters.to_date:
            conditions.append(
                [
                    "appointment_date",
                    "between",
                    [filters.get("from_date"), filters.get("to_date")],
                ]
            )
        if filters.company:
            conditions.append(["company", "=", filters.company])
            conditions.append(["insurance_company", "=", "NHIF"])
        if filters.status == "Open":
            conditions.append(["status", "=", "Open"])
        if filters.status == "Closed":
            conditions.append(["status", "=", "Closed"])
        return conditions
