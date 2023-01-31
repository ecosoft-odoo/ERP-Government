# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class BudgetAllocation(models.Model):
    _inherit = "budget.allocation"

    analytic_tag_all_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        compute="_compute_all_data",
        relation="budget_allocation_tag_rel",
        column1="allocation_id",
        column2="tag_id",
        help="Used to provide a list of analytic tags in an excel sheet",
    )
    analytic_ids = fields.Many2many(
        comodel_name="account.analytic.account",
        compute="_compute_all_data",
        relation="budget_allocation_analytic_rel",
        column1="allocation_id",
        column2="analytic_id",
        help="Used to provide a list of analytic accounts in an excel sheet",
    )
    fund_ids = fields.Many2many(
        comodel_name="budget.source.fund",
        compute="_compute_all_data",
        relation="budget_allocation_fund_rel",
        column1="allocation_id",
        column2="fund_id",
        help="Used to provide a list of source of funds in an excel sheet",
    )

    def _compute_all_data(self):
        all_analytic_tag = self.env["account.analytic.tag"].search([])
        all_fund = self.env["budget.source.fund"].search([])
        Analytic = self.env["account.analytic.account"]
        for rec in self:
            all_analytic = Analytic.search(
                [
                    ("bm_date_to", ">=", rec.budget_period_id.bm_date_from),
                    ("bm_date_from", "<=", rec.budget_period_id.bm_date_to),
                ]
            )
            rec.analytic_tag_all_ids = [(6, 0, all_analytic_tag.ids)]
            rec.analytic_ids = [(6, 0, all_analytic.ids)]
            rec.fund_ids = [(6, 0, all_fund.ids)]
