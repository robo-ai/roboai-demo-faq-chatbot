## channels_teams (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_teams: Do you integrate with Microsoft Teams?   <!-- predicted: channels_teams: Do you integrate with [Microsoft Teams]{"entity": "bot_channel", "value": "teams"}? -->
    - slot{"bot_channel": "teams"}
    - utter_channels_teams   <!-- predicted: action_default_fallback -->


## channels_web (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_web: Web integration   <!-- predicted: channels_web: [Web]{"entity": "bot_channel", "value": "web"} integration -->
    - slot{"bot_channel": "web"}
    - utter_channels_web   <!-- predicted: action_default_fallback -->


## channels_whatsapp (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_whatsapp: I want to have a robo with whatsapp   <!-- predicted: channels_whatsapp: I want to have a robo with [whatsapp](bot_channel) -->
    - slot{"bot_channel": "whatsapp"}
    - utter_channels_whatsapp


## comment_hot (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* comment_hot: You sound like you are sexy.   <!-- predicted: comment_hot: You sound like you are [sexy]{"entity": "bot_received_emotion", "value": "hot"}. -->
    - slot{"bot_received_emotion": "hot"}
    - utter_comment_hot   <!-- predicted: action_default_fallback -->


## comment_positive (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* comment_positive: You are amazing.   <!-- predicted: comment_positive: You are [amazing]{"entity": "bot_received_emotion", "value": "positive"}. -->
    - slot{"bot_received_emotion": "positive"}
    - utter_comment_positive   <!-- predicted: action_default_fallback -->


## comment_smart (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* comment_smart: You are very wise.   <!-- predicted: bot_intelligence: You are very [wise]{"entity": "bot_received_emotion", "value": "smart"}. -->
    - slot{"bot_received_emotion": "smart"}
    - utter_comment_smart   <!-- predicted: action_default_fallback -->


## contacts_generic_Munich (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* contacts_generic: Contact details of the company.
    - utter_contacts_generic
* office_address_Munich: [Germany]{"entity": "company_cities_address", "value": "munich"}
    - slot{"company_cities_address": "munich"}
    - utter_contacts_address_munich   <!-- predicted: action_default_fallback -->


## demo_automotive (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_automotive: Can I see your car demos?   <!-- predicted: demo_automotive: Can I see your [car]{"entity": "bot_sector", "value": "automotive"} demos? -->
    - slot{"bot_sector": "automotive"}
    - utter_demo_automotive


## demo_banking (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_banking: I would like to see some banking demos.   <!-- predicted: demo_banking: I would like to see some [banking](bot_sector) demos. -->
    - slot{"bot_sector": "banking"}
    - utter_demo_banking


## demo_general_banking (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_general: Demos
    - utter_demo_general
* demo_banking: I would like to see some banking demos.   <!-- predicted: demo_banking: I would like to see some [banking](bot_sector) demos. -->
    - slot{"bot_sector": "banking"}
    - utter_demo_banking


## demo_general_insurance (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_general: Demos
    - utter_demo_general
* demo_insurance: Could you show me insurance demos?   <!-- predicted: demo_insurance: Could you show me [insurance](bot_sector) demos? -->
    - slot{"bot_sector": "insurance"}
    - utter_demo_insurance


## demo_general_telco (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_general: Demos
    - utter_demo_general
* demo_telco: Can you show me some telco demos?   <!-- predicted: demo_telco: Can you show me some [telco](bot_sector) demos? -->
    - slot{"bot_sector": "telco"}
    - utter_demo_telco


## demo_insurance (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_insurance: Could you show me insurance demos?   <!-- predicted: demo_insurance: Could you show me [insurance](bot_sector) demos? -->
    - slot{"bot_sector": "insurance"}
    - utter_demo_insurance


## demo_telco (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* demo_telco: Can you show me some telco demos?   <!-- predicted: demo_telco: Can you show me some [telco](bot_sector) demos? -->
    - slot{"bot_sector": "telco"}
    - utter_demo_telco


## features_date (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* features_date: Today is which date?
    - utter_features_date   <!-- predicted: action_get_date -->


## features_time (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* features_time: Tell me the hours.
    - utter_features_time   <!-- predicted: action_get_time -->


## insurance_advantages (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* insurance_advantages: I would like to know the advantages of insurance chatbot   <!-- predicted: insurance_advantages: I would like to know the advantages of [insurance chatbot]{"entity": "bot_sector", "value": "insurance"} -->
    - slot{"bot_sector": "insurance"}
    - utter_insurance_advantages


## insurance_uses (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* insurance_uses: Insurance use cases   <!-- predicted: insurance_uses: [Insurance]{"entity": "bot_sector", "value": "insurance"} use cases -->
    - slot{"bot_sector": "insurance"}
    - utter_insurance_uses


## social_media_facebook (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* social_media_facebook: Where are you on the facebook?   <!-- predicted: social_media_facebook: Where are you on the [facebook](bot_social_media)? -->
    - slot{"bot_social_media": "facebook"}
    - utter_social_media_facebook   <!-- predicted: action_default_fallback -->


## social_media_generic (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* social_media_generic: Can I find you on social media?   <!-- predicted: social_media_generic: Can I find you on [social media]{"entity": "bot_social_media", "value": "generic"}? -->
    - slot{"bot_social_media": "generic"}
    - utter_social_media_generic


## social_media_linkedin (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* social_media_linkedin: Can I find robo on linkedin?   <!-- predicted: social_media_linkedin: Can I find robo on [linkedin](bot_social_media)? -->
    - slot{"bot_social_media": "linkedin"}
    - utter_social_media_linkedin


## solutions_automotive (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* solutions_automotive: What are the advantages of using a car solution   <!-- predicted: solutions_automotive: What are the advantages of using a [car]{"entity": "bot_sector", "value": "automotive"} solution -->
    - slot{"bot_sector": "automotive"}
    - utter_solutions_automotive   <!-- predicted: action_default_fallback -->


## solutions_banking (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* solutions_banking: How can I use the banking solution   <!-- predicted: solutions_banking: How can I use the [banking](bot_sector) solution -->
    - slot{"bot_sector": "banking"}
    - utter_solutions_banking   <!-- predicted: action_default_fallback -->


## solutions_insurance (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* solutions_insurance: Insurance solution advantages   <!-- predicted: solutions_insurance: [Insurance]{"entity": "bot_sector", "value": "insurance"} solution advantages -->
    - slot{"bot_sector": "insurance"}
    - utter_solutions_insurance


## solutions_telco (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* solutions_telco: What are the advantages of using a telco solution   <!-- predicted: solutions_telco: What are the advantages of using a [telco](bot_sector) solution -->
    - slot{"bot_sector": "telco"}
    - utter_solutions_telco


## telco_advantages (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* telco_advantages: Are there advantages for telecommunication robos?   <!-- predicted: telco_advantages: Are there advantages for [telecommunication]{"entity": "bot_sector", "value": "telco"} robos? -->
    - slot{"bot_sector": "telco"}
    - utter_telco_advantages


## telco_uses (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* telco_uses: What can a telecommunication robo offer?   <!-- predicted: telco_uses: What can a [telecommunication]{"entity": "bot_sector", "value": "telco"} robo offer? -->
    - slot{"bot_sector": "telco"}
    - utter_telco_uses


## user_angry (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* user_angry: I totally hate you.   <!-- predicted: user_hate: I totally hate you. -->
    - utter_user_angry   <!-- predicted: utter_user_hate -->


## bot_costs (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* bot_costs: Tell me your price.
    - utter_bot_costs   <!-- predicted: action_default_fallback -->


## automotive_uses (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* automotive_advantages: Automobile robo benefits   <!-- predicted: automotive_advantages: [Automobile robo]{"entity": "bot_sector", "value": "automotive"} benefits -->
    - slot{"bot_sector": "automotive"}
    - utter_automotive_advantages   <!-- predicted: action_default_fallback -->


## A basic end-to-end test (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* start: $start-dialogue
    - action_check_Bot_Introduced
    - utter_greeting_hello_introduced_false   <!-- predicted: action_default_fallback -->
* start: $start
    - utter_greeting_hello_introduced_true   <!-- predicted: action_check_Bot_Introduced -->


## automotive_advantages (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* automotive_advantages: Automotive bot benefits   <!-- predicted: automotive_advantages: [Automotive bot]{"entity": "bot_sector", "value": "automotive"} benefits -->
    - slot{"bot_sector": "automotive"}
    - utter_automotive_advantages   <!-- predicted: action_default_fallback -->


## bot_intelligence (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* bot_intelligence: Are you a brainy?
    - utter_bot_intelligence   <!-- predicted: action_default_fallback -->


## automotive_uses (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* automotive_uses: What can an vehicle robo do?   <!-- predicted: automotive_uses: What can an [vehicle robo]{"entity": "bot_sector", "value": "automotive"} do? -->
    - slot{"bot_sector": "automotive"}
    - utter_automotive_uses   <!-- predicted: action_default_fallback -->


## bot_sexual (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* bot_sexual: I wanna flirt with you.   <!-- predicted: bot_sexual: I wanna [flirt]{"entity": "bot_received_emotion", "value": "sexual"} with you. -->
    - slot{"bot_received_emotion": "sexual"}
    - utter_bot_sexual   <!-- predicted: action_default_fallback -->


## banking_advantages (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* banking_advantages: Banking bot advantages   <!-- predicted: banking_advantages: [Banking bot]{"entity": "bot_sector", "value": "banking"} advantages -->
    - slot{"bot_sector": "banking"}
    - utter_banking_advantages   <!-- predicted: action_default_fallback -->


## business_bi (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* business_bi: Business intelligence applications   <!-- predicted: business_bi: [Business intelligence]{"entity": "bot_business_sector", "value": "bi"} applications -->
    - slot{"bot_business_sector": "bi"}
    - utter_business_bi   <!-- predicted: action_default_fallback -->


## business_cms (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* business_cms: Content management system   <!-- predicted: business_cms: [Content management system]{"entity": "bot_business_sector", "value": "cms"} -->
    - slot{"bot_business_sector": "cms"}
    - utter_business_cms   <!-- predicted: action_default_fallback -->


## business_crm (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* business_crm: Customercentric relationship management system   <!-- predicted: business_crm: [Customercentric relationship management]{"entity": "bot_business_sector", "value": "crm"} system -->
    - slot{"bot_business_sector": "crm"}
    - utter_business_crm   <!-- predicted: action_default_fallback -->


## business_ecommerce (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* business_ecommerce: Solutions for shop online   <!-- predicted: business_ecommerce: Solutions for [shop online]{"entity": "bot_business_sector", "value": "ecommerce"} -->
    - slot{"bot_business_sector": "ecommerce"}
    - utter_business_ecommerce   <!-- predicted: action_default_fallback -->


## business_erp (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* business_erp: GRP system   <!-- predicted: business_erp: [GRP]{"entity": "bot_business_sector", "value": "erp"} system -->
    - slot{"bot_business_sector": "erp"}
    - utter_business_erp


## banking_uses (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* banking_uses: What can a banking bot offer?   <!-- predicted: banking_uses: What can a [banking bot]{"entity": "bot_sector", "value": "banking"} offer? -->
    - slot{"bot_sector": "banking"}
    - utter_banking_uses


## channels_alexa (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_alexa: Alexa chatbot   <!-- predicted: channels_alexa: [Alexa]{"entity": "bot_channel", "value": "alexa"} chatbot -->
    - slot{"bot_channel": "alexa"}
    - utter_channels_alexa


## channels_apple (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_apple: I want to have a bot in apple business   <!-- predicted: channels_apple: I want to have a bot in [apple business]{"entity": "bot_channel", "value": "apple"} -->
    - slot{"bot_channel": "apple"}
    - utter_channels_apple


## channels_call (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_call: phone call bot   <!-- predicted: channels_call: [phone call]{"entity": "bot_channel", "value": "call"} bot -->
    - slot{"bot_channel": "call"}
    - utter_channels_call   <!-- predicted: action_default_fallback -->


## channels_google_business (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_google_business: Can I have a robo on the google business?   <!-- predicted: channels_google_business: Can I have a robo on the [google business](bot_channel)? -->
    - slot{"bot_channel": "google business"}
    - utter_channels_google_business


## channels_google_home (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_google_home: Google home channel   <!-- predicted: channels_google_home: [Google home]{"entity": "bot_channel", "value": "google home"} channel -->
    - slot{"bot_channel": "google home"}
    - utter_channels_google_home


## channels_instagram (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_instagram: Insta messaging channel   <!-- predicted: channels_instagram: [Insta]{"entity": "bot_social_media", "value": "instagram"} messaging channel -->
    - slot{"bot_social_media": "instagram"}
    - utter_channels_instagram


## channels_messenger (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_messenger: I want to have a bot on messenger   <!-- predicted: channels_messenger: I want to have a bot on [messenger](bot_channel) -->
    - slot{"bot_channel": "messenger"}
    - utter_channels_messenger   <!-- predicted: action_default_fallback -->


## channels_mobile (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_mobile: Can I have a chatbot on mobile app?   <!-- predicted: channels_mobile: Can I have a chatbot on [mobile app]{"entity": "bot_channel", "value": "mobile"}? -->
    - slot{"bot_channel": "mobile"}
    - utter_channels_mobile   <!-- predicted: action_default_fallback -->


## channels_rcs (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_rcs: I want to have a robo with RCS   <!-- predicted: channels_rcs: I want to have a robo with [RCS]{"entity": "bot_channel", "value": "rcs"} -->
    - slot{"bot_channel": "rcs"}
    - utter_channels_rcs


## channels_skype (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_skype: Can I use Skype with a robo?   <!-- predicted: channels_skype: Can I use [Skype]{"entity": "bot_channel", "value": "skype"} with a robo? -->
    - slot{"bot_channel": "skype"}
    - utter_channels_skype   <!-- predicted: action_default_fallback -->


## channels_slack (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_slack: I want to have a bot on Slack   <!-- predicted: channels_slack: I want to have a bot on [Slack]{"entity": "bot_channel", "value": "slack"} -->
    - slot{"bot_channel": "slack"}
    - utter_channels_slack   <!-- predicted: action_default_fallback -->


## channels_sms (/tmp/tmpxv3vjlcc/899bd61ed44647388ca2479c1c9c6c0c_conversation_tests.md)
* channels_sms: Can I use the sms with a bot?   <!-- predicted: channels_sms: Can I use the [sms](bot_channel) with a bot? -->
    - slot{"bot_channel": "sms"}
    - utter_channels_sms   <!-- predicted: action_default_fallback -->


