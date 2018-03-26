from django import template
register = template.Library()

# from solve_activities.models import Solve

@register.simple_tag
def is_solved_by_user(problem, user):
    return problem.solved.filter(solver=user).exists()

@register.simple_tag
def count_problem_solves(problem, members):
    cnt = int(0)
    for member in members:
        print(member)
        if problem.solved.filter(solver=member.user).exists() == 1:
            cnt = cnt + 1
    return cnt
    # for member in members:
    #     print(member)
    #     if problem.solved.filter(solver=member.user).exists() == 1:
    #         return 1
    # return 0

# @register.simple_tag
# def isSolved(problem, user):
#     return Solve.objects.filter(solver_id=user, problem_id=problem).exists()
