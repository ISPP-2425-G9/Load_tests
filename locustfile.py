from admin.AdminCertificates import AdminDeathCertificates
from admin.AdminCompanies import AdminCompanies
from admin.AdminUsers import AdminUsers

from company.CompanyCompanies import CompanyCompanies
from company.CompanyUsers import CompanyUsers

from customer.CustomerCompanies import CustomerCompanies
from customer.CustomerDeathCertificates import CustomerDeathCertificates
from customer.CustomerEmergencyContacts import CustomerEmergencyContacts
from customer.CustomerMessages import CustomerMessages
from customer.CustomerReceivers import CustomerReceivers
from customer.CustomerTemplates import CustomerTemplates
from customer.CustomerUsers import CustomerUsers

from customer.CustomerPremiumEmergencyContacts import CustomerPremiumEmergencyContacts
from customer.CustomerPremiumMessages import CustomerPremiumMessages

from anonymous.status import checkStatus

# Admin module test

AdminUsers
AdminCompanies
AdminDeathCertificates

# Company module test

CompanyUsers
CompanyCompanies

# Customer free module test

CustomerCompanies
CustomerDeathCertificates
CustomerEmergencyContacts
CustomerMessages
CustomerReceivers
CustomerTemplates
CustomerUsers

# Customer premium module test

CustomerPremiumEmergencyContacts
CustomerPremiumMessages

# Anonymous module test

checkStatus
