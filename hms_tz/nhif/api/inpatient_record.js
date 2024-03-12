frappe.ui.form.on('Inpatient Record', {
    reset_admission_status_to_admission_scheduled: function (frm) {
        frm.set_value("status", "Admission Scheduled")
        frm.refresh_fields("status")
        frm.save()
    },
    refresh(frm) {
        // hide button to delete rows of occupancy
        $('*[data-fieldname="inpatient_occupancies"]').find('.grid-remove-rows').hide();
        $('*[data-fieldname="inpatient_occupancies"]').find('.grid-remove-all-rows').hide();

        //hide button to delete rows of consultancy
        $('*[data-fieldname="inpatient_consultancy"]').find('.grid-remove-rows').hide();
        $('*[data-fieldname="inpatient_consultancy"]').find('.grid-remove-all-rows').hide();

        frm.get_field("inpatient_occupancies").grid.cannot_add_rows = true;
        frm.get_field("inpatient_consultancy").grid.cannot_add_rows = true;

        if (!frm.doc.insurance_subscription) {
            frm.add_custom_button(__("Create Invoice"), () => {
                create_sales_invoice(frm);
            });
            frm.add_custom_button(__("Make Deposit"), () => {
                make_deposit(frm);
            }).addClass("font-weight-bold");
        }
    },
    onload(frm) {
        frm.get_field("inpatient_occupancies").grid.cannot_add_rows = true;
        frm.get_field("inpatient_consultancy").grid.cannot_add_rows = true;
    }
});

frappe.ui.form.on('Inpatient Occupancy', {
    form_render(frm, cdt, cdn) {
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-delete-row').hide();
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-duplicate-row').hide();
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-move-row').hide();
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-append-row').hide();
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-insert-row-below').hide();
        frm.fields_dict.inpatient_occupancies.grid.wrapper.find('.grid-insert-row').hide();
    },
    inpatient_occupancies_move: (frm, cdt, cdn) => {
        control_inpatient_record_move(frm, cdt, cdn);
    },
    is_confirmed: (frm, cdt, cdn) => {
        isConfirmed(frm, "inpatient_occupancies");
        validate_inpatient_balance_vs_inpatient_cost(frm);
    },
});

const control_inpatient_record_move = (frm, cdt, cdn) => {
    let row = frappe.get_doc(cdt, cdn);
    frm.reload_doc();
    frappe.throw(__(`This line should not be moved`));

};

frappe.ui.form.on('Inpatient Consultancy', {
    form_render(frm, cdt, cdn) {
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-delete-row').hide();
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-duplicate-row').hide();
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-move-row').hide();
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-append-row').hide();
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-insert-row-below').hide();
        frm.fields_dict.inpatient_consultancy.grid.wrapper.find('.grid-insert-row').hide();
    },

    is_confirmed: (frm, cdt, cdn) => {
        isConfirmed(frm, "inpatient_consultancy");
        validate_inpatient_balance_vs_inpatient_cost(frm);
    },
});

var make_deposit = (frm) => {
    let d = new frappe.ui.Dialog({
        title: "Patient Deposit",
        fields: [
            {
                label: "Deposit Amount",
                fieldname: "deposit_amount",
                fieldtype: "Currency",
                description: "make sure you write the correct amount",
                reqd: 1,
            },
            {
                label: "Reference Number",
                fieldname: "reference_number",
                fieldtype: "Data",
            },
            {
                fieldname: "md_cb",
                fieldtype: "Column Break"
            },
            {
                label: "Mode of Payment",
                fieldname: "mode_of_payment",
                fieldtype: "Link",
                options: "Mode of Payment",
                reqd: 1,
                "description": "make sure you select the correct mode of payment",
            },
            {
                fieldname: "reference_date",
                fieldtype: "Date",
                label: "Reference Date",
            }
        ],
        size: "large", // small, large, extra-large 
        primary_action_label: 'Submit',
        primary_action(values) {
            console.log(values);
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Mode of Payment",
                    filters: { name: values.mode_of_payment },
                    fieldname: ["type"]
                },
            }).then((r) => {
                if (r.message) {
                    if (r.message.type != "Cash" && !values.reference_number) {
                        frappe.msgprint({
                            title: __("Reference Number is required"),
                            indicator: 'red',
                            message: __("Reference Number is required for non cash payments,<br>please enter reference number or change mode of payment to cash")
                        })
                    } else if (r.message.type != "Cash" && !values.reference_date) {
                        frappe.msgprint({
                            title: __("Reference Date is required"),
                            indicator: 'red',
                            message: __("Reference Date is required for non cash payments,<br>please enter reference date or change mode of payment to cash")
                        })
                    } else {
                        d.hide();
                        frappe.call({
                            method: "hms_tz.nhif.api.inpatient_record.make_deposit",
                            args: {
                                inpatient_record: frm.doc.name,
                                deposit_amount: values.deposit_amount,
                                mode_of_payment: values.mode_of_payment,
                                reference_number: values.reference_number,
                                reference_date: values.reference_date,
                            },
                            freeze: true,
                            freeze_message: __('<i class="fa fa-spinner fa-spin fa-4x"></i>'),
                        }).then((r) => {
                            if (r.message) {
                                frm.reload_doc();
                            }
                        });
                    }
                }
            });
        }
    });

    d.show();
}

var create_sales_invoice = (frm) => {
    let filters = {
        "patient": frm.doc.patient,
        "appointment_no": frm.doc.patient_appointment,
        "inpatient_record": frm.doc.name,
        "company": frm.doc.company,
    }
    frappe.call({
        method: "hms_tz.nhif.api.inpatient_record.create_sales_invoice",
        args: {
            args: filters
        },
        freeze: true,
        freeze_message: __('<i class="fa fa-spinner fa-spin fa-4x"></i>'),
    }).then((r) => {
        if (r.message) {
            frappe.set_route("Form", "Sales Invoice", r.message);
        }
    });
}

var isConfirmed = (frm, fieldname) => {
    frappe.call({
        method: 'hms_tz.nhif.api.inpatient_record.confirmed',
        args: {
            company: frm.doc.company,
            appointment: frm.doc.patient_appointment,
            insurance_company: frm.doc.insurance_company,
        },
        callback: function (r) {
            if (r.message) {
                frm.refresh_field(fieldname);
                frm.reload_doc();
            }
        }
    });
}

var validate_inpatient_balance_vs_inpatient_cost = (frm) => {
    if (!frm.doc.insurance_subscription){
        frappe.call({
            method: 'hms_tz.nhif.api.inpatient_record.validate_inpatient_balance_vs_inpatient_cost',
            args: {
                patient: frm.doc.patient,
                inpatient_record: frm.doc.name,
                patient_appointment: frm.doc.patient_appointment,
            },
            callback: function (r) {
                if (!r.message) {
                    frm.refresh_field("inpatient_consultancies");
                    frm.reload_doc();
                }
            }
        });
    }
}