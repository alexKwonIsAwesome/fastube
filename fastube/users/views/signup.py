from django.views.generic import View

from django.shortcuts import render


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(request,
                "users/signup.html",
                context={},
            )

    def post(self, request, *args, **kwargs):
        pass

