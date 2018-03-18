from django import template
register = template.Library()

from solve_activities.models import Solve

@register.simple_tag
def is_solved_by_user(problem, user):
    return problem.solved.filter(solver=user).exists()

@register.simple_tag
def isSolved(problem, user):
    return Solve.objects.filter(solver_id=user, problem_id=problem).exists()
