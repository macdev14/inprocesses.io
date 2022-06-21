from django.db import models
from django.urls import reverse
from apps.authentication.models import *
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField, BRStateField
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
import datetime as datetime2
from django.core.mail import send_mail