# Copyright 2023 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Install All Module
    module_egov_install = fields.Boolean(string="All Module eGov")
    module_egov_coa = fields.Boolean(string="Chart of Account")
    module_egov_config = fields.Boolean()
    # Structure
    module_account_asset_operating_unit = fields.Boolean()
    module_account_asset_operating_unit_access_all = fields.Boolean()
    module_account_asset_transfer_operating_unit = fields.Boolean()
    module_account_financial_report_operating_unit = fields.Boolean()
    module_account_operating_unit = fields.Boolean()
    module_account_operating_unit_access_all = fields.Boolean()
    module_account_payment_multi_deduction_operating_unit = fields.Boolean()
    module_agreement_legal_operating_unit = fields.Boolean()
    module_agreement_operating_unit = fields.Boolean()
    module_agreement_operating_unit_access_all = fields.Boolean()
    module_analytic_operating_unit = fields.Boolean()
    module_analytic_operating_unit_access_all = fields.Boolean()
    module_base_model_restrict_update = fields.Boolean()
    module_base_tier_validation_correction = fields.Boolean()
    module_base_tier_validation_report = fields.Boolean()
    module_base_user_role = fields.Boolean()
    module_budget_allocation_operating_unit = fields.Boolean()
    module_budget_allocation_operating_unit_access_all = fields.Boolean()
    module_budget_control_operating_unit = fields.Boolean()
    module_budget_control_operating_unit_access_all = fields.Boolean()
    module_contract_operating_unit = fields.Boolean()
    module_contract_operating_unit_access_all = fields.Boolean()
    module_hr_expense_operating_unit = fields.Boolean()
    module_hr_expense_operating_unit_access_all = fields.Boolean()
    module_hr_operating_unit = fields.Boolean()
    module_hr_operating_unit_access_all = fields.Boolean()
    module_l10n_th_account_tax_expense_operating_unit = fields.Boolean()
    module_mis_builder_operating_unit = fields.Boolean()
    module_mis_builder_operating_unit_access_all = fields.Boolean()
    module_operating_unit = fields.Boolean()
    module_operating_unit_access_all = fields.Boolean()
    module_purchase_deposit_operating_unit = fields.Boolean()
    module_purchase_operating_unit = fields.Boolean()
    module_purchase_operating_unit_access_all = fields.Boolean()
    module_purchase_request_operating_unit = fields.Boolean()
    module_purchase_request_operating_unit_access_all = fields.Boolean()
    module_purchase_request_to_requisition_operating_unit = fields.Boolean()
    module_purchase_requisition_operating_unit = fields.Boolean()
    module_purchase_requisition_operating_unit_access_all = fields.Boolean()
    module_purchase_stock_operating_unit = fields.Boolean()
    module_sale_operating_unit = fields.Boolean()
    module_sale_operating_unit_access_all = fields.Boolean()
    module_sale_stock_operating_unit = fields.Boolean()
    module_sales_team_operating_unit = fields.Boolean()
    module_stock_account_operating_unit = fields.Boolean()
    module_stock_operating_unit = fields.Boolean()
    module_stock_operating_unit_access_all = fields.Boolean()
    # Budgeting
    module_account_asset_fund = fields.Boolean()
    module_account_asset_transfer_budget_allocation = fields.Boolean()
    module_account_invoice_payment_retention_budget_control = fields.Boolean()
    module_account_payment_multi_deduction_activity = fields.Boolean()
    module_account_payment_multi_deduction_budget_allocation = fields.Boolean()
    module_base_tier_validation_check_budget = fields.Boolean()
    module_budget_activity = fields.Boolean()
    module_budget_activity_advance_clearing = fields.Boolean()
    module_budget_activity_contract = fields.Boolean()
    module_budget_activity_contract_invoice_plan = fields.Boolean()
    module_budget_activity_expense = fields.Boolean()
    module_budget_activity_purchase = fields.Boolean()
    module_budget_activity_purchase_deposit = fields.Boolean()
    module_budget_activity_purchase_request = fields.Boolean()
    module_budget_activity_purchase_requisition = fields.Boolean()
    module_budget_allocation = fields.Boolean()
    module_budget_allocation_advance_clearing = fields.Boolean()
    module_budget_allocation_contract = fields.Boolean()
    module_budget_allocation_contract_invoice_plan = fields.Boolean()
    module_budget_allocation_department = fields.Boolean()
    module_budget_allocation_expense = fields.Boolean()
    module_budget_allocation_purchase = fields.Boolean()
    module_budget_allocation_purchase_deposit = fields.Boolean()
    module_budget_allocation_purchase_request = fields.Boolean()
    module_budget_allocation_purchase_requisition = fields.Boolean()
    module_budget_allocation_revision = fields.Boolean()
    module_budget_control = fields.Boolean()
    module_budget_control_account_asset_management = fields.Boolean()
    module_budget_control_advance_clearing = fields.Boolean()
    module_budget_control_contract = fields.Boolean()
    module_budget_control_expense = fields.Boolean()
    module_budget_control_purchase = fields.Boolean()
    module_budget_control_purchase_manual_currency = fields.Boolean()
    module_budget_control_purchase_request = fields.Boolean()
    module_budget_control_purchase_requisition = fields.Boolean()
    module_budget_control_revision = fields.Boolean()
    module_budget_control_revision_lock_amount = fields.Boolean()
    module_budget_plan = fields.Boolean()
    module_budget_plan_revision = fields.Boolean()
    module_budget_res_project_department = fields.Boolean()
    module_l10n_th_account_tax_expense_budget_allocation = fields.Boolean()
    module_l10n_th_gov_account_asset_management_budget_allocation = fields.Boolean()
    module_l10n_th_gov_purchase_agreement_budget_control = fields.Boolean()
    module_l10n_th_gov_hr_expense_activity = fields.Boolean()
    module_l10n_th_gov_hr_expense_budget_control = fields.Boolean()
    module_l10n_th_gov_purchase_guarantee_activity = fields.Boolean()
    module_l10n_th_gov_purchase_guarantee_budget_allocation = fields.Boolean()
    module_l10n_th_gov_purchase_guarantee_operating_unit = fields.Boolean()
    module_mis_builder = fields.Boolean()
    module_purchase_stock_budget_allocation = fields.Boolean()
    module_res_project = fields.Boolean()
    module_res_project_sequence = fields.Boolean()
    module_stock_budget_allocation = fields.Boolean()
    module_stock_request_budget_allocation = fields.Boolean()
    # Procurement
    module_l10n_th_gov_purchase_agreement = fields.Boolean()
    module_l10n_th_gov_purchase_report = fields.Boolean()
    module_l10n_th_gov_purchase_request = fields.Boolean()
    module_l10n_th_gov_purchase_guarantee = fields.Boolean()
    module_l10n_th_gov_work_acceptance = fields.Boolean()
    module_purchase_deposit = fields.Boolean()
    module_purchase_deposit_analytic = fields.Boolean()
    module_purchase_invoice_plan = fields.Boolean()
    module_purchase_invoice_plan_deposit = fields.Boolean()
    module_purchase_invoice_plan_retention = fields.Boolean()
    module_purchase_manual_currency = fields.Boolean()
    module_purchase_request = fields.Boolean()
    module_purchase_request_cancel_confirm = fields.Boolean()
    module_purchase_request_manual_currency = fields.Boolean()
    module_purchase_request_tier_validation = fields.Boolean()
    module_purchase_request_to_requisition_manual_currency = fields.Boolean()
    module_purchase_requisition_manual_currency = fields.Boolean()
    module_purchase_rfq_number = fields.Boolean()
    module_purchase_stock_analytic = fields.Boolean()
    module_purchase_tax_adjust = fields.Boolean()
    module_purchase_tier_validation = fields.Boolean()
    module_purchase_work_acceptance = fields.Boolean()
    module_purchase_work_acceptance_evaluation = fields.Boolean()
    module_purchase_work_acceptance_invoice_plan = fields.Boolean()
    module_purchase_work_acceptance_late_fines = fields.Boolean()
    module_purchase_work_acceptance_tier_validation = fields.Boolean()
    # Accounting
    module_account_check_date = fields.Boolean()
    module_account_check_payee = fields.Boolean()
    module_account_check_printing_report_base = fields.Boolean()
    module_account_financial_report = fields.Boolean()
    module_account_financial_report_extension = fields.Boolean()
    module_account_fiscal_year = fields.Boolean()
    module_account_journal_lock_date = fields.Boolean()
    module_account_lock_date_update = fields.Boolean()
    module_account_move_line_stock_info = fields.Boolean()
    module_account_payment_multi_deduction = fields.Boolean()
    module_account_reconciliation_widget = fields.Boolean()
    module_account_reconciliation_widget_extension = fields.Boolean()
    module_account_sequence_option = fields.Boolean()
    module_account_statement_import_txt_xlsx = fields.Boolean()
    module_account_usability = fields.Boolean()
    module_hr_expense_advance_clearing = fields.Boolean()
    module_hr_expense_advance_clearing_sequence = fields.Boolean()
    module_hr_expense_advance_overdue_reminder = fields.Boolean()
    module_hr_expense_cancel_confirm = fields.Boolean()
    module_hr_expense_cancel_policy = fields.Boolean()
    module_hr_expense_disable_confirm_duplicate = fields.Boolean()
    module_hr_expense_excluded_tax = fields.Boolean()
    module_hr_expense_exception = fields.Boolean()
    module_hr_expense_pay_to_vendor = fields.Boolean()
    module_hr_expense_payment = fields.Boolean()
    module_hr_expense_payment_widget_amount = fields.Boolean()
    module_hr_expense_sequence = fields.Boolean()
    module_hr_expense_sequence_option = fields.Boolean()
    module_hr_expense_tax_adjust = fields.Boolean()
    module_hr_expense_tier_validation = fields.Boolean()
    module_hr_expense_widget_o2m = fields.Boolean()
    module_l10n_th_account_tax = fields.Boolean()
    module_l10n_th_account_tax_branch_operating_unit = fields.Boolean()
    module_l10n_th_account_tax_branch_report = fields.Boolean()
    module_l10n_th_account_tax_expense = fields.Boolean()
    module_l10n_th_account_tax_multi = fields.Boolean()
    module_l10n_th_account_tax_report = fields.Boolean()
    module_l10n_th_account_wht_cert_form = fields.Boolean()
    module_l10n_th_bank = fields.Boolean()
    module_l10n_th_bank_payment_export = fields.Boolean()
    module_l10n_th_bank_payment_export_bbl = fields.Boolean()
    module_l10n_th_bank_payment_export_ktb = fields.Boolean()
    module_l10n_th_base_location = fields.Boolean()
    module_l10n_th_base_sequence = fields.Boolean()
    module_l10n_th_check_ktb = fields.Boolean()
    module_l10n_th_gov_hr_expense = fields.Boolean()
    module_l10n_th_gov_tier_validation = fields.Boolean()
    module_l10n_th_mis_report = fields.Boolean()
    module_partner_bank_code = fields.Boolean()
    module_sale_fixed_discount = fields.Boolean()
    module_sale_force_invoiced = fields.Boolean()
    module_sale_invoice_plan = fields.Boolean()
    module_sale_invoice_plan_retention = fields.Boolean()
    module_sale_management = fields.Boolean()
    module_sale_order_line_analytic = fields.Boolean()
    module_sale_order_line_stock_analytic = fields.Boolean()
    module_sale_stock_cancel_restriction = fields.Boolean()
    module_sale_tax_adjust = fields.Boolean()
    # Agreement & Contract
    module_agreement = fields.Boolean()
    module_agreement_legal = fields.Boolean()
    module_contract = fields.Boolean()
    module_contract_invoice_plan = fields.Boolean()
    module_contract_invoice_plan_selection = fields.Boolean()
    # Asset
    module_account_asset_compute_batch = fields.Boolean()
    module_account_asset_compute_batch_job = fields.Boolean()
    module_account_asset_from_expense = fields.Boolean()
    module_account_asset_low_value = fields.Boolean()
    module_account_asset_management = fields.Boolean()
    module_account_asset_transfer = fields.Boolean()
    module_l10n_th_account_asset_management = fields.Boolean()
    module_l10n_th_gov_account_asset_management = fields.Boolean()
    # Inventory
    module_l10n_th_gov_stock_request = fields.Boolean()
    module_stock_analytic = fields.Boolean()
    module_stock_card_report = fields.Boolean()
    module_stock_no_negative = fields.Boolean()
    module_stock_request = fields.Boolean()
    module_stock_request_separate_picking = fields.Boolean()
    # Optional - EGOV
    module_egov_budget_allocation_excel_import_export = fields.Boolean()
    module_egov_budget_control_excel_import_export = fields.Boolean()
    module_egov_hr_expense = fields.Boolean()
    module_egov_purchase = fields.Boolean()
    module_egov_purchase_request = fields.Boolean()
    module_egov_user_role = fields.Boolean()
    # Optional - Other App
    module_om_credit_limit = fields.Boolean()
