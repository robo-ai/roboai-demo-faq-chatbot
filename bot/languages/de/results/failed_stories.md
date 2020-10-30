## robo_cosibot (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* robo_cosibot: None   <!-- predicted: greeting_hello: None -->
    - utter_robo_cosibot   <!-- predicted: action_check_Bot_Introduced -->


## robo_handover (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* robo_handover: None   <!-- predicted: greeting_hello: None -->
    - utter_robo_handover   <!-- predicted: action_check_Bot_Introduced -->


## whatsapp_business_data_customer (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* whatsapp_business_data_customer: None   <!-- predicted: greeting_hello: None -->
    - utter_whatsapp_business_data_customer   <!-- predicted: action_check_Bot_Introduced -->


## comment_smart (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* comment_smart: None   <!-- predicted: greeting_hello: None -->
    - utter_comment_smart   <!-- predicted: action_check_Bot_Introduced -->


## contacts_address_evora (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* contacts_address_evora: Wie lautet eure Adresse in [Évora]{"entity": "company_cities_address", "value": "evora"}?   <!-- predicted: contacts_address_evora: Wie lautet eure Adresse in [Évora?](company_cities_address) -->
    - slot{"company_cities_address": "Évora?"}
    - utter_contacts_address_evora


## contacts_address_lisbon (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* contacts_address_lisbon: Wie lautet eure Adresse in [Lissabon]{"entity": "company_cities_address", "value": "lisbon"}?   <!-- predicted: contacts_address_lisbon: Wie lautet eure Adresse in [Lissabon?](company_cities_address) -->
    - slot{"company_cities_address": "Lissabon?"}
    - utter_contacts_address_lisbon


## contacts_address_munich (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* contacts_address_munich: Wie lautet eure Adresse in [München]{"entity": "company_cities_address", "value": "munich"}?   <!-- predicted: contacts_address_munich: Wie lautet eure Adresse in [München?](company_cities_address) -->
    - slot{"company_cities_address": "München?"}
    - utter_contacts_address_munich


## contacts_generic_evora (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* contacts_generic_evora: Wo kann ich euch in [Alentejo]{"entity": "company_cities_address", "value": "evora"} kontaktieren?
    - slot{"company_cities_address": "evora"}
    - utter_contacts_generic_evora   <!-- predicted: utter_contacts_address_evora -->


## contacts_generic_munich (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* contacts_generic_munich: Wo kann ich euch in [München]{"entity": "company_cities_address", "value": "munich"} kontaktieren?
    - slot{"company_cities_address": "munich"}
    - utter_contacts_generic_munich   <!-- predicted: utter_contacts_address_munich -->


## demo_insurance (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* demo_insurance: Kann ich [Versicherungs]{"entity": "bot_sector", "value": "insurance"}Demos sehen   <!-- predicted: demo_insurance: Kann ich VersicherungsDemos sehen -->
    - utter_demo_insurance


## start (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* start: /start-dialogue{"bot_introduced": "False"}   <!-- predicted: start-dialogue: /start-dialogue{"bot_introduced": "False"} -->
    - slot{"bot_introduced": "False"}
    - action_check_Bot_Introduced
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false


## features_date (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* features_date: Wann findet die CCW statt?
    - utter_features_date   <!-- predicted: action_get_date -->


## features_time (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* features_time: Können Sie mir die Uhrzeit schreiben?
    - utter_features_time   <!-- predicted: action_get_time -->


## greeting_hello (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* greeting_hello: Hallo
    - utter_greeting_hello   <!-- predicted: action_check_Bot_Introduced -->


## positive_feedback (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* positive_feedback: Sie machen das super.   <!-- predicted: comment_positive: Sie machen das super. -->
    - utter_positive_feedback   <!-- predicted: utter_comment_positive -->


## business_ecommerce (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* business_ecommerce: ECommerce   <!-- predicted: robo_prices: ECommerce -->
    - utter_business_ecommerce   <!-- predicted: action_default_fallback -->


## banking_uses (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* banking_uses: Was bieten [Banking]{"entity": "bot_sector", "value": "banking"}Chatbots?   <!-- predicted: banking_uses: Was bieten BankingChatbots? -->
    - utter_banking_uses


## ccw_about (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* ccw_about: Das CCW
    - utter_ccw_about   <!-- predicted: utter_platform_about -->


## ccw_date (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* ccw_date: None   <!-- predicted: greeting_hello: None -->
    - utter_ccw_date   <!-- predicted: action_check_Bot_Introduced -->


## ccw_place (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* ccw_place: CCW lokal.
    - utter_ccw_place   <!-- predicted: action_check_Bot_Introduced -->


## ccw_robo (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* ccw_robo: Nimmt robo.ai an der CCW teil?
    - utter_ccw_robo   <!-- predicted: action_default_fallback -->


## robo_about (/tmp/tmpcwwvprjy/bbad5b417d0c4a81a22c664a200f678f_conversation_tests.md)
* robo_about: InfoRobo.   <!-- predicted: vocative_help: InfoRobo. -->
    - utter_robo_about   <!-- predicted: utter_vocative_help -->


