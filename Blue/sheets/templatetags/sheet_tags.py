from django import template
register = template.Library()

# from solve_activities.models import Solve

@register.simple_tag
def is_solved_by_user(problem, user):
    return problem.solved.filter(solver=user).exists()

@register.simple_tag
def count_problem_solves(problem, members):
    cnt = int(0)
    for mem in members:
        if problem.solved.filter(solver=mem.member).exists() == 1:
            cnt = cnt + 1
    return cnt
