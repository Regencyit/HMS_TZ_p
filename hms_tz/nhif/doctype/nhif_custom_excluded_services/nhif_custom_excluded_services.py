# Copyright (c) 2022, Aakvatech and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import now_datetime
from frappe.model.document import Document

class NHIFCustomExcludedServices(Document):
	def validate(self):
		self.set_title()
		self.set_missing_values()
		
	def set_title(self):
		abbr_name = frappe.get_cached_value('Company', self.company, 'abbr')
		self.title = _('{0} - {1}').format(self.item, abbr_name)

	def set_missing_values(self):
		if not self.time_stamp:
			self.time_stamp = now_datetime()
		self.itemcode = frappe.get_value('Item Customer Detail', {'parent': self.item}, 'ref_code')
		if not self.itemcode:
			frappe.throw(_("refcode is not found on Item Customer Detail of Item doctype for item: {0}\
				please set it to proceed".format(frappe.bold(self.item))))

@frappe.whitelist()
def validate_item(company, item, name):
    record = frappe.get_value(
        "NHIF Custom Excluded Services",
        {"name": ["!=", name], "company": company, "item": item},
    )
    if record:
        return record


@frappe.whitelist()
def get_custom_excluded_services(company, item_code):
    custom_excluded_services = frappe.get_all(
        "NHIF Custom Excluded Services",
        filters={"company": company, "itemcode": item_code},
        fields=["excludedforproducts"],
    )
    if custom_excluded_services:
        return custom_excluded_services[0].excludedforproducts
