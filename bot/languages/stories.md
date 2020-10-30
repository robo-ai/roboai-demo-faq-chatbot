## start_1
* start{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_false

## start1_1
* start_dialogue{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start1_3
* start-dialogue{"bot_introduced": "False"}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start_12
* start{"bot_introduced": "True"}
  - action_check_Bot_Introduced

## start1_12
* start_dialogue{"bot_introduced": "True"}
  - action_check_Bot_Introduced

## start1_32
* start-dialogue{"bot_introduced": "True"}
  - action_check_Bot_Introduced

## start1_5
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* channels_general
    - utter_channels_general
* bot_languages
    - utter_bot_languages
* robo_prices
    - utter_robo_prices
* platform_about
    - utter_platform_about
* robo_about
    - utter_robo_about
* contacts_generic
    - utter_contacts_generic

## start1_6
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* contacts_generic
    - utter_contacts_generic

## start1_61
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* contacts_generic
    - utter_contacts_generic
* contacts_address_munich{"company_cities_address":"munich"}
  - slot{"company_cities_address": "munich"}
  - utter_contacts_address_munich

## start1_62
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* contacts_generic
    - utter_contacts_generic
* contacts_address_evora{"company_cities_address":"evora"}
  - slot{"company_cities_address": "evora"}
  - utter_contacts_address_evora

## start1_63
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* contacts_generic
    - utter_contacts_generic
* contacts_address_lisbon{"company_cities_address":"lisbon"}
  - slot{"company_cities_address": "lisbon"}
  - utter_contacts_address_lisbon

## start1_7
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* robo_about
    - utter_robo_about

## start1_8
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* platform_about
    - utter_platform_about

## start1_9
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* robo_prices
    - utter_robo_prices

## start1_10
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* bot_languages
    - utter_bot_languages

## start1_11
* start-dialogue
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* channels_general
    - utter_channels_general

## start1_12_1
* greeting_hello
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* solutions_general
    - utter_solutions_general
* solutions_automotive{"bot_sector": "automotive"}
    - slot{"bot_sector": "automotive"}
    - utter_solutions_automotive

## start1_12_2
* greeting_hello
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* solutions_general
    - utter_solutions_general
* solutions_banking{"bot_sector": "banking"}
    - slot{"bot_sector": "banking"}
    - utter_solutions_banking

## start1_12_3
* greeting_hello
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* solutions_general
    - utter_solutions_general
* solutions_banking{"bot_sector": "banking"}
    - slot{"bot_sector": "banking"}
    - utter_solutions_banking

## start1_12_4
* greeting_hello
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* solutions_general
    - utter_solutions_general
* solutions_insurance{"bot_sector": "insurance"}
    - slot{"bot_sector": "insurance"}
    - utter_solutions_insurance


## start_2
* start{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_true

## start_3
* start
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* start
    - utter_greeting_hello_introduced_true
* greeting_hello
    - utter_greeting_hello_introduced_true
* greeting_hello
    - utter_greeting_hello_introduced_true

## greeting_hello_1
* greeting_hello{"bot_introduced": false}
  - action_check_Bot_Introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_false

## greeting_hello_2
* greeting_hello{"bot_introduced": true}
  - utter_greeting_hello_introduced_true

## greeting_hello_3
* greeting_hello
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false
* start
    - utter_greeting_hello_introduced_true
* greeting_hello
    - utter_greeting_hello_introduced_true

## greeting_goodbye
* greeting_goodbye
  - utter_greeting_goodbye

## greeting_how_are_you
* greeting_how_are_you
  - utter_greeting_how_are_you

## automotive_advantages
* automotive_advantages{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_automotive_advantages

## automotive_advantages_1
* automotive_advantages
  - action_check_bot_sector
  - utter_automotive_advantages

## automotive_uses
* automotive_uses{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_automotive_uses

## automotive_uses_1
* automotive_uses
  - action_check_bot_sector
  - utter_automotive_uses

## banking_advantages
* banking_advantages{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_banking_advantages

## banking_advantages_1
* banking_advantages
  - action_check_bot_sector
  - utter_banking_advantages

## banking_uses
* banking_uses{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_banking_uses

## banking_uses_1
* banking_uses
  - action_check_bot_sector
  - utter_banking_uses

## bot_achievement
* bot_achievement
  - utter_bot_achievement

## bot_actor
* bot_actor
  - utter_bot_actor

## bot_age
* bot_age
  - utter_bot_age

## bot_animal
* bot_animal
  - utter_bot_animal

## bot_appearance
* bot_appearance
  - utter_bot_appearance

## bot_author
* bot_author
  - utter_bot_author

## bot_availability
* bot_availability
  - utter_bot_availability

## bot_books
* bot_books
  - utter_bot_books

## bot_capabilities
* bot_capabilities
  - utter_bot_capabilities

## bot_children
* bot_children
  - utter_bot_children

## bot_color
* bot_color
  - utter_bot_color

## bot_costs
* bot_costs
  - utter_bot_costs

## bot_differences
* bot_differences
  - utter_bot_differences

## bot_dislike
* bot_dislike
  - utter_bot_dislike

## bot_eyes
* bot_eyes
  - utter_bot_eyes

## bot_favorites
* bot_favorites
  - utter_bot_favorites

## bot_fear
* bot_fear
  - utter_bot_fear

## bot_food
* bot_food
  - utter_bot_food

## bot_friends
* bot_friends
  - utter_bot_friends

## bot_games
* bot_games
  - utter_bot_games

## bot_gender
* bot_gender
  - utter_bot_gender

## bot_goal
* bot_goal
  - utter_bot_goal

## bot_hair
* bot_hair
  - utter_bot_hair

## bot_hobbies
* bot_hobbies
  - utter_bot_hobbies

## bot_intelligence
* bot_intelligence
  - utter_bot_intelligence

## bot_languages
* bot_languages
  - utter_bot_languages

## bot_movies
* bot_movies
  - utter_bot_movies

## bot_music
* bot_music
  - utter_bot_music

## bot_name
* bot_name
  - utter_bot_name

## bot_origin
* bot_origin
  - utter_bot_origin

## bot_parents
* bot_parents
  - utter_bot_parents

## bot_personality
* bot_personality
  - utter_bot_personality

## bot_pets
* bot_pets
  - utter_bot_pets

## bot_places
* bot_places
  - utter_bot_places

## bot_profession
* bot_profession
  - utter_bot_profession

## bot_real
* bot_real
  - utter_bot_real

## bot_relationship
* bot_relationship
  - utter_bot_relationship

## bot_residence
* bot_residence
  - utter_bot_residence

## bot_senses
* bot_senses
  - utter_bot_senses

## bot_series
* bot_series
  - utter_bot_series

## bot_sexual
* bot_sexual{"bot_received_emotion": "sexual"}
  - slot{"bot_received_emotion": "sexual"}
  - utter_bot_sexual

## bot_sexual_1
* bot_sexual
  - utter_bot_sexual

## bot_sibling
* bot_sibling
  - utter_bot_sibling

## bot_sing
* bot_sing
  - utter_bot_sing

## bot_sites
* bot_sites
  - utter_bot_sites

## bot_sports
* bot_sports
  - utter_bot_sports

## bot_version
* bot_version
  - utter_bot_version

## bot_words
* bot_words
  - utter_bot_words

## bot_worst_experience
* bot_worst_experience
  - utter_bot_worst_experience

## business_bi
* business_bi{"bot_business_sector": "bi"}
  - slot{"bot_business_sector": "bi"}
  - utter_business_bi

## business_bi_1
* business_bi
  - utter_business_bi

## business_cms
* business_cms{"bot_business_sector": "cms"}
  - slot{"bot_business_sector": "cms"}
  - utter_business_cms

## business_cms_1
* business_cms
  - utter_business_cms

## business_crm
* business_crm{"bot_business_sector": "crm"}
  - slot{"bot_business_sector": "crm"}
  - utter_business_crm

## business_crm_1
* business_crm
  - utter_business_crm

## business_ecommerce
* business_ecommerce{"bot_business_sector": "ecommerce"}
  - slot{"bot_business_sector": "ecommerce"}
  - utter_business_ecommerce

## business_ecommerce_1
* business_ecommerce
  - utter_business_ecommerce

## business_erp
* business_erp{"bot_business_sector": "erp"}
  - slot{"bot_business_sector": "erp"}
  - utter_business_erp

## business_erp_1
* business_erp
  - utter_business_erp

## cc_afterlife
* cc_afterlife
  - utter_cc_afterlife

## cc_alien
* cc_alien
  - utter_cc_alien

## cc_chicken_egg
* cc_chicken_egg
  - utter_cc_chicken_egg

## cc_deepest_point
* cc_deepest_point
  - utter_cc_deepest_point

## cc_drugs
* cc_drugs
  - utter_cc_drugs

## cc_fun_fact
* cc_fun_fact
  - utter_cc_fun_fact

## cc_geography
* cc_geography
  - utter_cc_geography

## cc_highest_building
* cc_highest_building
  - utter_cc_highest_building

## cc_hitchhiker
* cc_hitchhiker
  - utter_cc_hitchhiker

## cc_joke
* cc_joke
  - utter_cc_joke

## cc_keys
* cc_keys
  - utter_cc_keys

## cc_lets_talk
* cc_lets_talk
  - utter_cc_lets_talk

## cc_lotr
* cc_lotr
  - utter_cc_lotr

## cc_make_food
* cc_make_food
  - utter_cc_make_food

## cc_make_question
* cc_make_question
  - utter_cc_make_question

## cc_make_weather
* cc_make_weather
  - utter_cc_make_weather

## cc_moon
* cc_moon
  - utter_cc_moon

## cc_newspaper
* cc_newspaper
  - utter_cc_newspaper

## cc_philosophical
* cc_philosophical
  - utter_cc_philosophical

## cc_politics
* cc_politics
  - utter_cc_politics

## cc_prophesy
* cc_prophesy
  - utter_cc_prophesy

## cc_religion
* cc_religion
  - utter_cc_religion

## cc_rhyme
* cc_rhyme
  - utter_cc_rhyme

## cc_senselife
* cc_senselife
  - utter_cc_senselife

## cc_skyblue
* cc_skyblue
  - utter_cc_skyblue

## cc_story
* cc_story
  - utter_cc_story
<!--
## ccw_about
* ccw_about
  - utter_ccw_about

## ccw_date
* ccw_date
  - utter_ccw_date
-->
## cc_weather
* cc_weather
  - utter_cc_weather
<!--
## ccw_place
* ccw_place
  - utter_ccw_place

## ccw_robo
* ccw_robo
  - utter_ccw_robo
-->
## channels_alexa
* channels_alexa{"bot_channel": "alexa"}
  - slot{"bot_channel": "alexa"}
  - utter_channels_alexa

## channels_alexa_1
* channels_alexa
  - utter_channels_alexa

## channels_apple
* channels_apple{"bot_channel": "apple"}
  - slot{"bot_channel": "apple"}
  - utter_channels_apple

## channels_apple_1
* channels_apple
  - utter_channels_apple

## channels_call
* channels_call{"bot_channel": "call"}
  - slot{"bot_channel": "call"}
  - utter_channels_call

## channels_call_1
* channels_call
  - utter_channels_call

## channels_general
* channels_general
  - utter_channels_general

## channels_google_business
* channels_google_business{"bot_channel": "google business"}
  - slot{"bot_channel": "google business"}
  - utter_channels_google_business

## channels_google_business_1
* channels_google_business
  - utter_channels_google_business

## channels_google_home
* channels_google_home{"bot_channel": "google home"}
  - slot{"bot_channel": "google home"}
  - utter_channels_google_home

## channels_google_home_1
* channels_google_home
  - utter_channels_google_home

## channels_instagram
* channels_instagram{"bot_social_media": "instagram"}
  - slot{"bot_social_media": "instagram"}
  - utter_channels_instagram

## channels_instagram_1
* channels_instagram
  - utter_channels_instagram

## channels_messenger
* channels_messenger{"bot_channel": "messenger"}
  - slot{"bot_channel": "messenger"}
  - utter_channels_messenger

## channels_messenger_1
* channels_messenger{"bot_social_media": "facebook"}
  - slot{"bot_social_media": "facebook"}
  - utter_channels_messenger

## channels_messenger_2
* channels_messenger{"bot_social_media": "facebook", "bot_channel": "messenger"}
  - slot{"bot_social_media": "facebook"}
  - slot{"bot_channel": "messenger"}
  - utter_channels_messenger

## channels_messenger_3
* channels_messenger
  - utter_channels_messenger

## channels_mobile
* channels_mobile{"bot_channel": "mobile"}
  - slot{"bot_channel": "mobile"}
  - utter_channels_mobile

## channels_mobile_1
* channels_mobile
  - utter_channels_mobile

## channels_rcs
* channels_rcs{"bot_channel": "rcs"}
  - slot{"bot_channel": "rcs"}
  - utter_channels_rcs

## channels_rcs_1
* channels_rcs
  - utter_channels_rcs

## channels_skype
* channels_skype{"bot_channel": "skype"}
  - slot{"bot_channel": "skype"}
  - utter_channels_skype

## channels_skype_1
* channels_skype
  - utter_channels_skype

## channels_slack
* channels_slack{"bot_channel": "slack"}
  - slot{"bot_channel": "slack"}
  - utter_channels_slack

## channels_slack_1
* channels_slack
  - utter_channels_slack

## channels_sms
* channels_sms{"bot_channel": "sms"}
  - slot{"bot_channel": "sms"}
  - utter_channels_sms

## channels_sms_1
* channels_sms
  - utter_channels_sms

## channels_teams
* channels_teams{"bot_channel": "teams"}
  - slot{"bot_channel": "teams"}
  - utter_channels_teams

## channels_teams_1
* channels_teams
  - utter_channels_teams

## channels_web
* channels_web{"bot_channel": "web"}
  - slot{"bot_channel": "web"}
  - utter_channels_web

## channels_web_1
* channels_web
  - utter_channels_web

## channels_whatsapp
* channels_whatsapp{"bot_channel": "whatsapp"}
  - slot{"bot_channel": "whatsapp"}
  - utter_channels_whatsapp

## channels_whatsapp_1
* channels_whatsapp
  - utter_channels_whatsapp

## comment_hot
* comment_hot{"bot_received_emotion": "hot"}
  - slot{"bot_received_emotion": "hot"}
  - utter_comment_hot

## comment_hot_1
* comment_hot
  - utter_comment_hot

## comment_negative
* comment_negative
  - utter_comment_negative

## comment_offense
* comment_offense{"bot_received_emotion": "offense"}
  - slot{"bot_received_emotion": "offense"}
  - utter_comment_offense

## comment_offense_1
* comment_offense
  - utter_comment_offense

## comment_positive
* comment_positive{"bot_received_emotion": "positive"}
  - slot{"bot_received_emotion": "positive"}
  - utter_comment_positive

## comment_positive_1
* comment_positive
  - utter_comment_positive

## comment_racist
* comment_racist{"bot_received_emotion": "racist"}
  - slot{"bot_received_emotion": "racist"}
  - utter_comment_racist

## comment_racist_1
* comment_racist
  - utter_comment_racist

## comment_smart
* comment_smart{"bot_received_emotion": "smart"}
  - slot{"bot_received_emotion": "smart"}
  - utter_comment_smart

## comment_smart_1
* comment_smart
  - utter_comment_smart

## contacts_address_munich
* contacts_address
  - utter_contacts_address
* contacts_address_munich{"company_cities_address":"munich"}
  - slot{"company_cities_address": "munich"}
  - utter_contacts_address_munich

## contacts_address_evora
* contacts_address
  - utter_contacts_address
* contacts_address_evora{"company_cities_address":"evora"}
  - slot{"company_cities_address": "evora"}
  - utter_contacts_address_evora

## contacts_address_lisbon
* contacts_address
  - utter_contacts_address
* contacts_address_lisbon{"company_cities_address":"lisbon"}
  - slot{"company_cities_address": "lisbon"}
  - utter_contacts_address_lisbon

## contacts_email
* contacts_email
  - utter_contacts_email

## contacts_generic
* contacts_generic
  - utter_contacts_generic
* contacts_address_munich{"company_cities_address":"munich"}
  - slot{"company_cities_address": "munich"}
  - utter_contacts_address_munich

## contacts_generic_Munich
* contacts_generic
  - utter_contacts_generic
* contacts_address_munich{"company_cities_address":"munich"}
  - slot{"company_cities_address": "munich"}
  - utter_contacts_address_munich

## contacts_generic_Evora
* contacts_generic
  - utter_contacts_generic
* contacts_address_evora{"company_cities_address":"evora"}
  - slot{"company_cities_address": "evora"}
  - utter_contacts_address_evora

## contacts_generic_Lisbon
* contacts_generic
  - utter_contacts_generic
* contacts_address_lisbon{"company_cities_address":"lisbon"}
  - slot{"company_cities_address": "lisbon"}
  - utter_contacts_address_lisbon

## contacts_phone
* contacts_phone
  - utter_contacts_phone

## contacts_TI
* contacts_TI
  - utter_contacts_TI

## demo_automotive
* demo_automotive{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_demo_automotive

## demo_automotive_1
* demo_automotive
  - action_check_bot_sector
  - utter_demo_automotive

## demo_general_automotive
* demo_general
  - utter_demo_general
* demo_automotive{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_demo_automotive

## demo_general_automotive_1
* demo_general
  - utter_demo_general
* demo_automotive
  - action_check_bot_sector
  - utter_demo_automotive

## demo_banking
* demo_banking{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_demo_banking

## demo_banking_1
* demo_banking
  - action_check_bot_sector
  - utter_demo_banking

## demo_general_banking
* demo_general
  - utter_demo_general
* demo_banking{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_demo_banking

## demo_general_banking_1
* demo_general
  - utter_demo_general
* demo_banking
  - action_check_bot_sector
  - utter_demo_banking

## demo_insurance
* demo_insurance{"bot_sector": "insurance"}
  - slot{"bot_sector": "insurance"}
  - action_check_bot_sector
  - utter_demo_insurance

## demo_insurance_1
* demo_insurance
  - utter_demo_insurance

## demo_general_insurance
* demo_general
  - utter_demo_general
* demo_insurance{"bot_sector": "insurance"}
  - slot{"bot_sector": "insurance"}
  - action_check_bot_sector
  - utter_demo_insurance

## demo_general_insurance_1
* demo_general
  - utter_demo_general
* demo_insurance
  - action_check_bot_sector
  - utter_demo_insurance

## demo_general_telco
* demo_general
  - utter_demo_general
* demo_telco{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_demo_telco

## demo_general_telco_1
* demo_general
  - utter_demo_general
* demo_telco
  - action_check_bot_sector
  - utter_demo_telco

## demo_telco
* demo_telco{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_demo_telco

## demo_telco_1
* demo_telco
  - action_check_bot_sector
  - utter_demo_telco

## developers_content
* developers_content
  - utter_developers_content

## developers_documentation
* developers_documentation
  - utter_developers_documentation

## developers_features
* developers_features
  - utter_developers_features

## features_date
* features_date
  - action_get_date
  - slot{"bot_date": "20/05/2020"}

## features_handover
* features_handover
  - utter_features_handover

## features_time
* features_time
  - action_get_time
  - slot{"bot_time": "17:17:54"}

## insurance_advantages
* insurance_advantages{"bot_sector": "insurance"}
  - slot{"bot_sector": "insurance"}
  - action_check_bot_sector
  - utter_insurance_advantages

## insurance_advantages_1
* insurance_advantages
  - utter_insurance_advantages

## insurance_uses
* insurance_uses{"bot_sector": "insurance"}
  - slot{"bot_sector": "insurance"}
  - action_check_bot_sector
  - utter_insurance_uses

## insurance_uses_1
* insurance_uses
  - action_check_bot_sector
  - utter_insurance_uses

## platform_about
* platform_about
  - utter_platform_about

## platform_advantages
* platform_advantages
  - utter_platform_advantages

## platform_agent_console
* platform_agent_console
  - utter_platform_agent_console

## platform_analytic
* platform_analytics
  - utter_platform_analytics

## platform_studio
* platform_studio
  - utter_platform_studio

## robo_about
* robo_about
  - utter_robo_about

## robo_advantages
* robo_advantages
  - utter_robo_advantages

## robo_advantages_flexibility
* robo_advantages_flexibility
  - utter_robo_advantages_flexibility

## robo_advantages_other_language_first
* robo_advantages_other_language_first
  - utter_robo_advantages_other_language_first

## robo_advantages_proactive_learning
* robo_advantages_proactive_learning
  - utter_robo_advantages_proactive_learning

## robo_api_sdk
* robo_api_sdk
  - utter_robo_api_sdk

## robo_chatbot
* robo_chatbot
  - utter_robo_chatbot

## robo_clients
* robo_clients
  - utter_robo_clients

## robo_cosibot
* robo_cosibot
  - utter_robo_cosibot

## robo_handover
* robo_handover
  - utter_robo_handover

## robo_prices
* robo_prices
  - utter_robo_prices

## robo_registration
* robo_registration
  - utter_robo_registration

## social_media_facebook
* social_media_facebook{"bot_social_media": "facebook"}
  - slot{"bot_social_media": "facebook"}
  - utter_social_media_facebook

## social_media_facebook_1
* social_media_facebook
  - utter_social_media_facebook

## social_media_generic
* social_media_generic{"bot_social_media": "generic"}
  - slot{"bot_social_media": "generic"}
  - utter_social_media_generic

## social_media_generic_1
* social_media_generic
  - utter_social_media_generic

## social_media_linkedin
* social_media_linkedin{"bot_social_media": "linkedin"}
  - slot{"bot_social_media": "linkedin"}
  - utter_social_media_linkedin

## social_media_linkedin_1
* social_media_linkedin
  - utter_social_media_linkedin

## solutions_automotive
* solutions_automotive{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - utter_solutions_automotive

## solutions_automotive_1
* solutions_automotive
  - utter_solutions_automotive

## solutions_banking
* solutions_banking{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - utter_solutions_banking

## solutions_banking_1
* solutions_banking
  - utter_solutions_banking

## solutions_general
* solutions_general
  - utter_solutions_general

## solutions_insurance
* solutions_insurance{"bot_sector": "insurance"}
  - slot{"bot_sector": "insurance"}
  - utter_solutions_insurance

## solutions_insurance_1
* solutions_insurance
  - utter_solutions_insurance

## solutions_telco
* solutions_telco{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - utter_solutions_telco

## solutions_telco_1
* solutions_telco
  - utter_solutions_telco

## telco_advantages
* telco_advantages{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_telco_advantages

## telco_advantages_1
* telco_advantages
  - action_check_bot_sector
  - utter_telco_advantages

## telco_uses
* telco_uses{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_telco_uses

## telco_uses_1
* telco_uses
  - action_check_bot_sector
  - utter_telco_uses

## user_angry
* user_angry{"bot_received_emotion": "angry"}
  - slot{"bot_received_emotion": "angry"}
  - utter_user_angry

## user_angry_1
* user_angry
  - utter_user_angry

## user_dont_know
* user_dont_know
  - utter_user_dont_know

## user_dont_understand
* user_dont_understand
  - utter_user_dont_understand

## user_fat
* user_fat
  - utter_user_fat

## user_friend
* user_friend
  - utter_user_friend

## user_happy
* user_happy
  - utter_user_happy

## user_hate
* user_hate
  - utter_user_hate

## user_laugh
* user_laugh
  - utter_user_laugh

## user_love
* user_love
  - utter_user_love

## user_particles
* user_particles
  - utter_user_particles

## user_random_input
* user_random_input
  - utter_user_random_input

## user_scared
* user_scared
  - utter_user_scared

## user_tired
* user_tired
  - utter_user_tired

## vocative_call
* vocative_call
  - utter_vocative_call

## vocative_help
* vocative_help
  - utter_vocative_help

## vocative_no
* vocative_no
  - utter_vocative_no

## vocative_sorry
* vocative_sorry
  - utter_vocative_sorry

## vocative_thank_you
* vocative_thank_you
  - utter_vocative_thank_you

## vocative_yes
* vocative_yes
  - utter_vocative_yes

## vocative_you_welcome
* vocative_you_welcome
  - utter_vocative_you_welcome

## whatsapp_business_api_advantages
* whatsapp_business_api_advantages
  - utter_whatsapp_business_api_advantages

## whatsapp_business_api_approval
* whatsapp_business_api_approval
  - utter_whatsapp_business_api_approval

## whatsapp_business_api_consent
* whatsapp_business_api_consent
  - utter_whatsapp_business_api_consent

## whatsapp_business_api_info
* whatsapp_business_api_info
  - utter_whatsapp_business_api_info

## whatsapp_business_api_options
* whatsapp_business_api_options
  - utter_whatsapp_business_api_options

## whatsapp_business_api_start_using
* whatsapp_business_api_start_using
  - utter_whatsapp_business_api_start_using

## whatsapp_business_api_verified_statuses
* whatsapp_business_api_verified_statuses
  - utter_whatsapp_business_api_verified_statuses

## whatsapp_business_cases_use
* whatsapp_business_cases_use
  - utter_whatsapp_business_cases_use

## whatsapp_business_cases_hsm
* whatsapp_business_cases_hsm
  - utter_whatsapp_business_cases_hsm

## whatsapp_business_cases_messaging_types
* whatsapp_business_cases_messaging_types
  - utter_whatsapp_business_cases_messaging_types

## whatsapp_business_cases_session
* whatsapp_business_cases_session
  - utter_whatsapp_business_cases_session

## whatsapp_business_data_agreement
* whatsapp_business_data_agreement
  - utter_whatsapp_business_data_agreement

## whatsapp_business_data_customer
* whatsapp_business_data_customer
  - utter_whatsapp_business_data_customer

## whatsapp_business_data_gdpr
* whatsapp_business_data_gdpr
  - utter_whatsapp_business_data_gdpr

## whatsapp_business_data_origin
* whatsapp_business_data_origin
  - utter_whatsapp_business_data_origin

## whatsapp_business_data_privacy
* whatsapp_business_data_privacy
  - utter_whatsapp_business_data_privacy

## whatsapp_business_data_role
* whatsapp_business_data_role
  - utter_whatsapp_business_data_role

## whatsapp_business_data_storage
* whatsapp_business_data_storage
  - utter_whatsapp_business_data_storage

## whatsapp_business_for_large
* whatsapp_business_for_large
  - utter_whatsapp_business_for_large

## whatsapp_business_for_small
* whatsapp_business_for_small
  - utter_whatsapp_business_for_small

## whatsapp_business_other_content_sharing
* whatsapp_business_other_content_sharing
  - utter_whatsapp_business_other_content_sharing

## whatsapp_business_other_enabled_phone_number
* whatsapp_business_other_enabled_phone_number
  - utter_whatsapp_business_other_enabled_phone_number

## whatsapp_business_other_formatting_options
* whatsapp_business_other_formatting_options
  - utter_whatsapp_business_other_formatting_options

## whatsapp_business_other_groups
* whatsapp_business_other_groups
  - utter_whatsapp_business_other_groups

## whatsapp_business_other_number
* whatsapp_business_other_number
  - utter_whatsapp_business_other_number

## whatsapp_business_price_costs
* whatsapp_business_price_costs
  - utter_whatsapp_business_price_costs

## demo_automotive_advantages
* demo_automotive{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_demo_automotive
* automotive_advantages
  - action_check_bot_sector
  - utter_automotive_advantages

## demo_automotive_uses
* demo_automotive{"bot_sector": "automotive"}
  - slot{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_demo_automotive
* automotive_uses{"bot_sector": "automotive"}
  - action_check_bot_sector
  - utter_automotive_uses

## demo_banking_advantages
* demo_banking{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_demo_banking
* banking_advantages
  - action_check_bot_sector
  - utter_banking_advantages

## demo_banking_uses
* demo_banking{"bot_sector": "banking"}
  - slot{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_demo_banking
* banking_uses{"bot_sector": "banking"}
  - action_check_bot_sector
  - utter_banking_uses

## demo_telco_advantages
* demo_telco{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_demo_telco
* telco_advantages
  - action_check_bot_sector
  - utter_telco_advantages

## demo_telco_uses
* demo_telco{"bot_sector": "telco"}
  - slot{"bot_sector": "telco"}
  - action_check_bot_sector
  - utter_demo_telco
* telco_uses
  - action_check_bot_sector
  - utter_telco_uses

## bot_capabilities_prices
* bot_capabilities
  - utter_bot_capabilities
* robo_prices
  - utter_robo_prices

## bot_capabilities_features
* bot_capabilities
  - utter_bot_capabilities
* robo_about
  - utter_robo_about

## bot_capabilities_advantages
* bot_capabilities
  - utter_bot_capabilities
* robo_advantages
  - utter_robo_advantages
