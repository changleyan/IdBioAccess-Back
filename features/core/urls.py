from config.urls import routers
from features.core.views import *

routers.register('user', UserApiView, basename='user_api')

routers.register('area', AreaApiView, basename='area_api')

routers.register('donation', DonationApiView, basename='donation_api')

routers.register('initial-state', InitialStateApiView, basename='initial_state_api')

routers.register('union-section', UnionSectionApiView, basename='union_section_api')

routers.register('affiliate', AffiliateApiView, basename='affiliate_api')

routers.register('act', ActApiView, basename='act_api')

routers.register('agreement', AgreementApiView, basename='agreement_api')

routers.register('approach', ApproachApiView, basename='approach_api')

routers.register('deposit-finance', DepositFinanceApiView, basename='deposit_finance_api')

routers.register('contribution-deposit', ContributionDepositApiView, basename='contribution_deposit_api')

urlpatterns = []
