import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute():
     properties = [
        {
            "doctype": "Patient Appointment",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "HLC-APP-.YYYY.-"
        },
        {
            "doctype": "Lab Test",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "HLC-LAB-.YYYY.-"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "HLC-INP-.YYYY.-"
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "naming_series",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Practitioner",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "HLC-PRAC-.YYYY.-"
        },
        {
            "doctype": "NHIF Patient Claim",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "NPC-.#########"
        },
        {
            "doctype": "NHIF Response Log",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "NHIF-RES-.YY.-.########"
        },
        {
            "doctype": "Practitioner Availability Type",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_rename",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination Template",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_rename",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination Template",
            "fieldname": "disabled",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination Template",
            "fieldname": "item",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "patient_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "patient",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "patient_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "healthcare_practitioner",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "practitioner_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medication Change Request",
            "fieldname": "practitioner_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "sb_comments",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Lab Test",
            "fieldname": "lab_test_comment",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "source",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "company",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "practitioner",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "patient_age",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "ref_docname.patient_age"
        },
        {
            "doctype": "Lab Test",
            "fieldname": "insurance_section",
            "property": "hidden",
            "value": 0,
            "property_type": "Check"
        },
        {
            "doctype": "Lab Test",
            "fieldname": "insurance_subscription",
            "property": "read_only",
            "value": 1,
            "property_type": "Check"
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "practitioner",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "radiology_examination_template",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "medical_department",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "patient",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "source",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "start_date",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "start_time",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination", 
            "fieldname": "insurance_section",
            "property": "hidden",
            "value": 0,
            "property_type": "Check"
        },
        {
            "doctype": "Radiology Examination", 
            "fieldname": "insurance_subscription",
            "property": "read_only",
            "value": 1,
            "property_type": "Check"
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "procedure_template",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "company",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "patient",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "source",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "insurance_subscription",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "patient_age",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "ref_docname.patient_age"
        },
        {
            "doctype": "Clinical Procedure", 
            "fieldname": "insurance_section",
            "property": "hidden",
            "value": 0,
            "property_type": "Check"
        },
        {
            "doctype": "Therapy Plan",
            "fieldname": "patient",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Therapy Plan",
            "fieldname": "company",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "expected_discharge",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "discharge_ordered_date",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "admitted_datetime",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "status",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "order",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "order_date",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "priority",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "staff_role",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "order_doctype",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "practitioner",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval: doc.patient"
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "practitioner",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Therapy Plan",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "practitioner_availability",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "duration",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "insurance_claim",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "insurance_company",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "claim_status",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "status",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "practitioner_name",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "department",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "practitioner",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "patient",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "patient_name",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "sb_source",
            "property": "depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "naming_series",
            "property": "options",
            "property_type": "Text",
            "value": "HLC-CPR-.YYYY.-"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "encounter_date",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "encounter_time",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment_type",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "practitioner",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "practitioner",
            "property": "default",
            "property_type": "Text",
            "value": "Direct Cash"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient_age",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "appointment.patient_age"
        },
        {
            "doctype": "Patient",
            "fieldname": "personal_and_social_history",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "risk_factors",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Practitioner Availability",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_copy",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Practitioner Availability",
            "fieldname": "practitioner",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "patient",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": "eval: doc.appointment"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment_type",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval: doc.encounter_type != \"Direct Cash\";\n"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment_type",
            "property": "default",
            "property_type": "Text",
            "value": "Direct Cash"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient",
            "property": "default",
            "property_type": "Text",
            "value": ""
        },
        {
            "doctype": "Patient",
            "fieldname": "allergies",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medical_history",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "surgical_history",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Descriptive Test Result",
            "fieldname": "result_value",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "result_component_option.result_component_option"
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "tongue",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "abdomen",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "reflexes",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "for_doctype": True,
            "fieldname": "",
            "property": "sort_field",
            "property_type": "Data",
            "value": "naming_series"
        },
        {
            "doctype": "Patient Encounter",
            "for_doctype": True,
            "fieldname": "",
            "property": "sort_order",
            "property_type": "Data",
            "value": "ASC"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_source",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "procedures_section",
            "property": "label",
            "property_type": "Data",
            "value": " Procedure Order"
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "paid_amount",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "duration",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "service_unit",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "allergy_medical_and_surgical_history",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "height",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Appointment Type",
            "for_doctype": True,
            "fieldname": "",
            "property": "sort_field",
            "property_type": "Data",
            "value": "name"
        },
        {
            "doctype": "Appointment Type",
            "for_doctype": True,
            "fieldname": "",
            "property": "sort_order",
            "property_type": "Data",
            "value": "ASC"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "investigations_section",
            "property": "label",
            "property_type": "Data",
            "value": "LAB ORDERS"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "lab_test_prescription",
            "property": "label",
            "property_type": "Data",
            "value": "Lab Tests"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "medication_section",
            "property": "label",
            "property_type": "Data",
            "value": "Medication Orders"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "drug_prescription",
            "property": "label",
            "property_type": "Data",
            "value": "Items"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "diagnosis",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "investigations_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "radiology_orders_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "procedures_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "rehabilitation_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "diet_recommendation_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "medication_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "procedures_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!doc.procedure_prescription"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "medication_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!doc.drug_prescription"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "rehabilitation_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!doc.therapy_plan"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "radiology_orders_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!doc.radiology_procedure_prescription"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "investigations_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!(doc.lab_test_prescription || doc.previous_lab_prescription)"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "company",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "encounter_details_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "drug_prescription",
            "property": "permlevel",
            "property_type": "Int",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "dosage_form",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "section_break_3",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "diet_recommendation_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "encounter_comment",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "codification",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "physical_examination",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "diagnosis",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "diagnosis_in_print",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "radiology_examination_template",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval:doc.patient && !doc.procedure_template && !doc.therapy_type"
        },
        {
            "doctype": "Patient",
            "fieldname": "patient_details",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "for_doctype": True,
            "fieldname": "",
            "property": "search_fields",
            "property_type": "Data",
            "value": "patient_name,insurance_company_name,coverage_plan_card_number,coverage_plan_name"
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "tc_name",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "terms",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "tc_name",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": ""
        },
        {
            "doctype": "Radiology Examination Template",
            "for_doctype": True,
            "fieldname": "",
            "property": "quick_entry",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Medication",
            "for_doctype": True,
            "fieldname": "",
            "property": "search_fields",
            "property_type": "Data",
            "value": "national_drug_code, generic_name, strength_text"
        },
        {
            "doctype": "Patient",
            "for_doctype": True,
            "fieldname": "",
            "property": "quick_entry",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "section_break_19",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "codification",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "comment",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "drug_code.default_comments"
        },
        {
            "doctype": "Healthcare Service Insurance Coverage",
            "fieldname": "end_date",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Insurance Coverage",
            "fieldname": "is_active",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "appointment",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "insurance_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "insurance_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "dosage",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "period",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "company",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "source",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": "eval:doc.company"
        },
        {
            "doctype": "Patient",
            "fieldname": "triage",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "invite_user",
            "property": "default",
            "property_type": "Text",
            "value": 0
        },
        {
            "doctype": "Patient",
            "fieldname": "territory",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "default_currency",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "default_price_list",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "patient_name",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "customer",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "gender",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "insurance_company_name",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "insurance_company_customer",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "country",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "more_info",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "patient_details_with_formatting"
        },
        {
            "doctype": "Item",
            "fieldname": "customer_details",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Item",
            "fieldname": "customer_details",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval:!doc.customer_items"
        },
        {
            "doctype": "Patient Appointment",
            "for_doctype": True,
            "fieldname": "",
            "property": "image_field",
            "property_type": "Data",
            "value": "patient_image2"
        },
        {
            "doctype": "Vital Signs",
            "for_doctype": True,
            "fieldname": "",
            "property": "image_field",
            "property_type": "Data",
            "value": "image"
        },
        {
            "doctype": "Patient Encounter",
            "for_doctype": True,
            "fieldname": "",
            "property": "image_field",
            "property_type": "Data",
            "value": "image"
        },
        {
            "doctype": "Lab Prescription",
            "fieldname": "lab_test_comment",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval:doc.override_subscription == 1 && doc.prescribe != 1;"
        },
        {
            "doctype": "Radiology Procedure Prescription",
            "fieldname": "radiology_test_comment",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval:doc.override_subscription == 1 && doc.prescribe != 1;"
        },
        {
            "doctype": "Procedure Prescription",
            "fieldname": "comments",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval:doc.override_subscription == 1 && doc.prescribe != 1;"
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "comment",
            "property": "mandatory_depends_on",
            "property_type": "Data",
            "value": "eval:doc.override_subscription == 1 && doc.prescribe != 1;"
        },
        {
            "doctype": "Healthcare Practitioner",
            "fieldname": "practitioner_name",
            "property": "in_global_search",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Healthcare Practitioner",
            "for_doctype": True,
            "fieldname": "",
            "property": "search_fields",
            "property_type": "Data",
            "value": "practitioner_name,mobile_phone,office_phone"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "symptoms_in_print",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_symptoms",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment_type",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Patient",
            "for_doctype": True,
            "fieldname": "",
            "property": "show_preview_popup",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "procedure_prescription",
            "property": "label",
            "property_type": "Data",
            "value": "Clinical Procedures"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment_type",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "mobile",
            "property": "reqd",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "for_doctype": True,
            "fieldname": "",
            "property": "search_fields",
            "property_type": "Data",
            "value": "patient_name,mobile,dob,old_hms_registration_no,insurance_card_detail"
        },
        {
            "doctype": "Practitioner Availability",
            "fieldname": "availability",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Practitioner Availability",
            "fieldname": "practitioner",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Practitioner Availability",
            "fieldname": "to_date",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "investigations_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "radiology_orders_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "procedures_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "medication_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "rehabilitation_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "diet_recommendation_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "radiology_procedures_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_drug_prescription",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "rehabilitation_section",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_procedures",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_test_prescription",
            "property": "collapsible",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "radiology_procedures_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.radiology_procedure_prescription && doc.previous_radiology_procedure_prescription && !(doc.radiology_procedure_prescription.length == 0 && doc.previous_radiology_procedure_prescription.length == 0)"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_drug_prescription",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.drug_prescription && doc.previous_drug_prescription && !(doc.drug_prescription.length == 0 && doc.previous_drug_prescription.length == 0)"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_procedures",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.procedure_prescription && doc.previous_procedure_prescription && !(doc.procedure_prescription.length == 0 && doc.previous_procedure_prescription.length == 0)"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "rehabilitation_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.therapies && doc.previous_therapy_plan_detail && !(doc.therapies.length == 0 && doc.previous_therapy_plan_detail.length == 0)"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "diet_recommendation_section",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.diet_recommendation && doc.diet_recommendation.length != 0"
        },
        {
            "doctype": "Patient",
            "fieldname": "patient_name",
            "property": "in_preview",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "allergies",
            "property": "in_preview",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medication",
            "property": "in_preview",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medical_history",
            "property": "in_preview",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "surgical_history",
            "property": "in_preview",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medication",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medical_history",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "appointment",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient_name",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "triage",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient_sex",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "company",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "medical_department",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "comment",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_test_prescription",
            "property": "collapsible_depends_on",
            "property_type": "Data",
            "value": "eval: doc.lab_test_prescription && doc.previous_lab_prescription && !(doc.lab_test_prescription.length == 0 && doc.previous_lab_prescription.length == 0)"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient_vitals_summary_section",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "patient_vitals",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "triage",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "inpatient_record",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "inpatient_status",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "sb_symptoms",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "symptoms",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "diagnosis",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "section_break_33",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice Item",
            "fieldname": "item_tax_template",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "item_code.default_tax_template"
        },
        {
            "doctype": "Practitioner Availability",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_rename",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Normal Test Result",
            "fieldname": "result_value",
            "property": "depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "item_code",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "item_name",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "rate",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "insurance_subscription",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "admission_encounter.insurance_subscription"
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "insurance_subscription",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "inpatient_occupancies",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "service_unit",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "left",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "check_out",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Record",
            "fieldname": "references",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "left",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "check_out",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "drug_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Exercise",
            "fieldname": "difficulty_level",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "origin_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Normal Test Result",
            "fieldname": "normal_range",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "encounter_time",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "insurance_subscription",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "naming_series",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medication",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "patient_name",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "patient.patient_name"
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "insurance_section",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "dosage",
            "property": "reqd",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "period",
            "property": "reqd",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Appointment",
            "fieldname": "appointment_type",
            "property": "default",
            "property_type": "Text",
            "value": "Outpatient Visit"
        },
        {
            "doctype": "Descriptive Test Result",
            "fieldname": "lab_test_particulars",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": ""
        },
        {
            "doctype": "Descriptive Test Result",
            "fieldname": "lab_test_particulars",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "Patient",
            "fieldname": "medication",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "medical_history",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "personal_and_social_history",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Patient",
            "fieldname": "sb_relation",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "allergy_medical_and_surgical_history",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "radiology_examination_template",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "appointment",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "procedure_template",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "practitioner_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "patient_name",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "patient.patient_name"
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "patient_name",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "sb_source",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "insurance_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "patient",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "drug_prescription_created",
            "property": "label",
            "property_type": "Data",
            "value": "Drug Prescription Created"
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "drug_prescription_created",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "is_pos",
            "property": "default",
            "property_type": "Text",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "risk_factors",
            "property": "collapsible",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Descriptive Test Result",
            "fieldname": "result_value",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Examination",
            "fieldname": "patient_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "is_return",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "set_posting_time",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "accounting_dimensions_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "customer_po_details",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "set_warehouse",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "time_sheet_list",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "loyalty_points_redemption",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "column_break4",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "debit_to",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "sales_team_section_break",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "section_break2",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "subscription_section",
            "property": "read_only",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice Item",
            "fieldname": "item_code",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice Item",
            "fieldname": "qty",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Sales Invoice Item",
            "fieldname": "rate",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Chronic Medications",
            "fieldname": "dosage",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Chronic Medications",
            "fieldname": "period",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "description",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "uom",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "rate",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "section_break_6",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "qty",
            "property": "columns",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "warehouse",
            "property": "columns",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Delivery Note Item",
            "fieldname": "batch_no",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "patient",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Subscription",
            "fieldname": "insurance_company_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "order_group",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_copy",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Clinical Procedure",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_copy",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "patient",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "order_group",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Order",
            "fieldname": "patient_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_rename",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "customer_po_details",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "update_stock",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "address_and_contact",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "shipping_rule",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "tax_category",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "more_info",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "subscription_section",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "terms_section_break",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "edit_printing_settings",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "insurance_section",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "start_date",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "start_time",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "sample",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Clinical Procedure",
            "fieldname": "sb_refs",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient",
            "fieldname": "first_name",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": "eval: doc.mobile"
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "invoiced",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Lab Test",
            "fieldname": "section_break_50",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Insurance Coverage",
            "fieldname": "healthcare_service",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Service Insurance Coverage",
            "fieldname": "healthcare_service_template",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Claim",
            "fieldname": "healthcare_service_type",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Claim",
            "fieldname": "healthcare_service_type",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Claim",
            "fieldname": "service_template",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Claim",
            "fieldname": "service_template",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Healthcare Insurance Company",
            "fieldname": "customer",
            "property": "read_only",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "drug_code",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "dosage",
            "property": "columns",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "period",
            "property": "columns",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "comment",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "interval",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "interval_uom",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "quantity",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "quantity",
            "property": "columns",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Vital Signs",
            "fieldname": "patient_name",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Medical Code",
            "fieldname": "description",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Dosage Strength",
            "fieldname": "strength",
            "property": "label",
            "property_type": "Data",
            "value": "Quantity in PCs"
        },
        {
            "doctype": "Patient",
            "fieldname": "customer_group",
            "property": "default",
            "property_type": "Text",
            "value": "Patient"
        },
        {
            "doctype": "Prescription Dosage",
            "for_doctype": True,
            "fieldname": "",
            "property": "quick_entry",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Shift Type",
            "fieldname": "last_sync_of_checkin",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "POS Profile",
            "fieldname": "update_stock",
            "property": "default",
            "property_type": "Text",
            "value": 0
        },
        {
            "doctype": "POS Profile",
            "fieldname": "warehouse",
            "property": "depends_on",
            "property_type": "Data",
            "value": ""
        },
        {
            "doctype": "Lab Test",
            "fieldname": "practitioner",
            "property": "in_standard_filter",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Order",
            "fieldname": "due_date",
            "property": "print_hide",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Sales Order",
            "fieldname": "payment_schedule",
            "property": "print_hide",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "due_date",
            "property": "print_hide",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "payment_schedule",
            "property": "print_hide",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Purchase Order",
            "fieldname": "due_date",
            "property": "print_hide",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Purchase Order",
            "fieldname": "payment_schedule",
            "property": "print_hide",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Purchase Invoice",
            "fieldname": "payment_schedule",
            "property": "print_hide",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Fees",
            "fieldname": "receivable_account",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "fee_structure.receivable_account"
        },
        {
            "doctype": "Fees",
            "fieldname": "income_account",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "fee_structure.income_account"
        },
        {
            "doctype": "Fees",
            "fieldname": "cost_center",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "fee_structure.cost_center"
        },
        {
            "doctype": "Lab Test",
            "for_doctype": True,
            "fieldname": "",
            "property": "title_field",
            "property_type": "Data",
            "value": "title"
        },
        {
            "doctype": "Journal Entry",
            "fieldname": "letter_head",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "company.default_letter_head"
        },
        {
            "doctype": "NHIF Patient Claim",
            "fieldname": "authorization_no",
            "property": "permlevel",
            "property_type": "Int",
            "value": 0
        },
        {
            "doctype": "NHIF Patient Claim",
            "fieldname": "allow_changes",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "NHIF Patient Claim Disease",
            "fieldname": "disease_code",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": ""
        },
        {
            "doctype": "NHIF Patient Claim Disease",
            "fieldname": "disease_code",
            "property": "fetch_if_empty",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "NHIF Patient Claim",
            "fieldname": "authorization_no",
            "property": "read_only_depends_on",
            "property_type": "Data",
            "value": "eval: !doc.allow_changes"
        },
        {
            "doctype": "Inpatient Consultancy",
            "fieldname": "confirmed",
            "property": "hidden",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Inpatient Occupancy",
            "fieldname": "check_in",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "Inpatient Consultancy",
            "fieldname": "date",
            "property": "columns",
            "property_type": "Int",
            "value": "2"
        },
        {
            "doctype": "NHIF Patient Claim Disease",
            "fieldname": "date_created",
            "property": "permlevel",
            "property_type": "Int",
            "value": 1
        },
        {
            "doctype": "Therapy Type",
            "for_doctype": True,
            "fieldname": "",
            "property": "allow_rename",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Test",
            "fieldname": "patient_name",
            "property": "report_hide",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "payment_schedule_section",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Sales Invoice",
            "fieldname": "sales_team_section_break",
            "property": "depends_on",
            "property_type": "Data",
            "value": "eval: !in_list(frappe.user_roles, \"Healthcare Receptionist\")"
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "title",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "encounter_date",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "practitioner_name",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "finalized",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "medical_department",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 0
        },
        {
            "doctype": "Patient Encounter",
            "fieldname": "insurance_coverage_plan",
            "property": "in_list_view",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Lab Prescription",
            "fieldname": "invoiced",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Radiology Procedure Prescription",
            "fieldname": "invoiced",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Procedure Prescription",
            "fieldname": "invoiced",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Drug Prescription",
            "fieldname": "invoiced",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Therapy Plan Detail",
            "fieldname": "invoiced",
            "property": "allow_on_submit",
            "property_type": "Check",
            "value": 1
        },
        {
            "doctype": "Therapy Session", 
            "fieldname": "appointment",
            "property": "fetch_from",
            "value": "therapy_plan.hms_tz_appointment",
            "property_type": "Small Text"
        },
        {
            "doctype": "Therapy Session",
            "fieldname": "appointment",
            "property": "fetch_if_empty",
            "value": 1,
            "property_type": "Check"
        },
        {
            "doctype": "Therapy Session",
            "fieldname": "patient_age",
            "property": "fetch_from",
            "property_type": "Small Text",
            "value": "appointment.patient_age"
        },
     ]
     for property in properties:
        make_property_setter(
            property.get("doctype"),
            property.get("fieldname"),
            property.get("property"),
            property.get("value"),
            property.get("property_type"),
            for_doctype=True if property.get("for_doctype") else False,
            validate_fields_for_doctype=False
        )

frappe.db.commit()