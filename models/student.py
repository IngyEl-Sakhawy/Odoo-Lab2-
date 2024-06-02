from odoo import models, fields

class Student(models.Model):
    _name = 'your_module.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    enrollment_ids = fields.One2many('your_module.enrollment', 'student_id', string='Enrollments')
