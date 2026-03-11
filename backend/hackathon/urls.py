from django.urls import path
from .views import (

    # Health
    HealthView,

    # Employees
    EmployeeListView,
    EmployeeProfileView,

    # Reports
    HeadcountReportView,
    JoinersLeaversReportView,

    # Auth
    ApiLoginView,
    ApiRegisterView,
    ApiLogoutView,
    ApiForgotPasswordView,

    # Onboarding
    OnboardingChecklistView,
    OnboardingItemUpdateView,
    OnboardingDocumentView,
    OnboardingHRDashboardView,
    OnboardingInitView,

    # Role Change
    RoleChangeHistoryView,

    # Alerts
    AlertsView,
)

urlpatterns = [

    # Health
    path('health/', HealthView.as_view()),

    # Employees
    path('employees/', EmployeeListView.as_view()),
    path('employees/profile/<str:emp_id>/', EmployeeProfileView.as_view()),

    # Reports
    path('reports/headcount/', HeadcountReportView.as_view()),
    path('reports/joiners-leavers/', JoinersLeaversReportView.as_view()),

    # Onboarding
    path('onboarding/dashboard/', OnboardingHRDashboardView.as_view()),
    path('onboarding/document/', OnboardingDocumentView.as_view()),
    path('onboarding/document/<int:doc_id>/', OnboardingDocumentView.as_view()),
    path('onboarding/item/<int:item_id>/', OnboardingItemUpdateView.as_view()),
    path('onboarding/<str:emp_id>/init/', OnboardingInitView.as_view()),
    path('onboarding/<str:emp_id>/', OnboardingChecklistView.as_view()),

    # Authentication
    path('auth/login/', ApiLoginView.as_view()),
    path('auth/register/', ApiRegisterView.as_view()),
    path('auth/logout/', ApiLogoutView.as_view()),
    path('auth/forgot-password/', ApiForgotPasswordView.as_view()),

    # Role changes
    path('role-changes/<str:emp_id>/', RoleChangeHistoryView.as_view()),

    # Alerts
    path('alerts/', AlertsView.as_view()),
]