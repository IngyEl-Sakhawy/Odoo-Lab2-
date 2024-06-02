from odoo import models, fields

class Course(models.Model):
    _name = 'your_module.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    professor_id = fields.Many2one('res.partner', string='Professor')
    professor_email = fields.Char(string='Professor Email', related='professor_id.email', store=True)
    enrollment_ids = fields.One2many('your_module.enrollment', 'course_id', string='Enrollments')
    enrollment_count = fields.Integer(string='Enrollment Count', compute='_compute_enrollment_count')

    def _compute_enrollment_count(self):
        for record in self:
            record.enrollment_count = len(record.enrollment_ids)

    def action_open_course(self):
        self.write({'state': 'open'})

    def action_close_course(self):
        self.write({'state': 'closed'})
