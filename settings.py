
import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


CHANNEL_ROUTING = 'Empathy_Beget_Guile_Timer.routing.channel_routing'

SENTRY_DSN = 'http://ee3c5daaa6be43c38afbb2df55987f9f:14944f017bfe4f3ba49fe45d05133d63@sentry.otree.org/170'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

POINTS_DECIMAL_PLACES = 1

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'game', 'study', 'images'],
    'title': 'Behavioral Experiment (earn $0.80+bonus)',
    'description': 'This is part of a study in decision-making. In this activity, you will be grouped with another worker and finish three tasks.'
                   ,
    'frame_height': 500,
    'preview_template': 'Eye_Exam/Welcome.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 30*24, # 7 days
    'grant_qualification_id': '3JC3H4XMU9IAZNCLWX3MDLTQ42HC3S',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        qualification.Requirement('3JC3H4XMU9IAZNCLWX3MDLTQ42HC3S', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    # {
    #     'name': 'Empathy_Beget_Guile',
    #     'display_name': "Empathy Game(without Eye_Exam)",
    #     'num_demo_participants': 24,
    #     'app_sequence': ['Empathy_Beget_Guile'],
    # },
    {
        'name': 'Empathy_Beget_Guile_2',
        'display_name': "Empathy Game",
        'num_demo_participants': 24,
        'app_sequence': ['Eye_Exam', 'Empathy_Beget_Guile'],
    },
    # {
    #     'name': 'Eye_Exam',
    #     'display_name': "Eye Exam",
    #     'num_demo_participants': 24,
    #     'app_sequence': ['Eye_Exam'],
    # },
    # {
    #     'name': 'likert',
    #     'display_name': "likert",
    #     'num_demo_participants': 20,
    #     'app_sequence': ['likert'],
    # },
    # {
    #     'name': 'participant_generated_urn_1',
    #     'display_name': "Participant Generate Urn",
    #     'num_demo_participants': 8,
    #     'app_sequence': ['participant_generated_urn_1'],
    # },
    # {
    #     'name': 'covering_test',
    #     'display_name': "covering",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['covering_test']
    # },
    # {
    #     'name': 'Empathy',
    #     'display_name': "Empathy Beget Guile",
    #     'num_demo_participants': 30,
    #     'app_sequence': ['Empathy'],
    # },
    # {
    #     'name': 'likert',
    #     'display_name': "likert",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['likert'],
    # },
    # {
    #     'name': 'likertquest',
    #     'display_name': "likertquest",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['likertquest'],
    # },
    # {
    #     'name': 'anes2',
    #     'display_name': "Priming Treatment",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['anes2'],
    # },
    # {
    #     'name': 'anes',
    #     'display_name': "anes",
    #     'num_demo_participants': 10,
    #     'app_sequence': ['likert', 'donation'],
    # },
    # {
    #     'name': 'long_survey',
    #     'display_name': "long survey",
    #     'num_demo_participants': 20,
    #     'app_sequence': ['anes2', 'likert2', 'petition', 'donation', 'infoseeking', 'erase', 'item', 'ses'],
    # },
    # {
    #     'name': 'Empathy_Beget_Guile',
    #     'display_name': "Empathy",
    #     'num_demo_participants': 20,
    #     'app_sequence': ['Empathy_Beget_Guile'],
    # },
    # {
    #     'name': 'long_survey',
    #     'display_name': "long survey",
    #     'num_demo_participants': 40,
    #     'app_sequence': ['likert'],
    # },
    # {
    #     'name': 'erase',
    #     'display_name': "mouse tracking",
    #     'num_demo_participants': 5,
    #     'app_sequence': ['erase'],
    # },
    # {
    #     'name': 'long_survey_2',
    #     'display_name': "long survey 2",
    #     'num_demo_participants': 30,
    #     'app_sequence': ['anes2', 'likert'],
    # },
    # {
    #     'name': 'tracking',
    #     'display_name': "tracking",
    #     'num_demo_participants': 5,
    #     'app_sequence': ['erase'],
    # },
    # {
    #     'name': 'empathy_timer',
    #     'display_name': "Testing timeout on waiting page",
    #     'num_demo_participants': 20,
    #     'app_sequence': ['Empathy_Beget_Guile_Timer'],
    # },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
