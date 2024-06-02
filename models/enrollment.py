from odoo import models, fields

class Enrollment(models.Model):
    _name = 'your_module.enrollment'
    _description = 'Enrollment'

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    student_id = fields.Many2one('your_module.student', string='Student', required=True)
    course_id = fields.Many2one('your_module.course', string='Course', required=True)
    register_date = fields.Date(string='Register Date', default=fields.Date.today)

    @api.depends('student_id', 'register_date')
    def _compute_name(self):
        for record in self:
            if record.student_id and record.register_date:
                record.name = f"{record.student_id.name} ({record.register_date})"

    @api.model
    def create(self, vals):
        record = super(Enrollment, self).create(vals)
        record._compute_name()
        return record

    def write(self, vals):
        result = super(Enrollment, self).write(vals)
        self._compute_name()
        return result
