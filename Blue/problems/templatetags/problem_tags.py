from django import template
register = template.Library()

from solve_activities.models import Solve

@register.simple_tag
def is_solved_by_user(problem, user):
    return problem.solved.filter(solver=user).exists()
