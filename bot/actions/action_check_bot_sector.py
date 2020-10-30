from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction

MAPPER = {
    'banking': ['utter_banking_advantages', 'utter_banking_uses', 'utter_demo_banking'],
    'automotive': ['utter_automotive_advantages', 'utter_automotive_uses', 'utter_demo_automotive'],
    'telco': ['utter_telco_advantages', 'utter_telco_uses', 'utter_demo_telco'],
    'insurance': ['utter_insurance_advantages', 'utter_insurance_uses', 'utter_demo_insurance']
}


class CheckBotSector(Action):
    def name(self) -> Text:
        return "action_check_bot_sector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bot_sector = tracker.get_slot("bot_sector")

        if bot_sector is not None:
            intent = tracker.latest_message['intent'].get('name')
            if 'advantages' in intent:
                followup_action = MAPPER[bot_sector][0]
            elif 'uses' in intent:
                followup_action = MAPPER[bot_sector][1]
            elif 'demo' in intent:
                followup_action = MAPPER[bot_sector][2]
            else:
                followup_action = "utter_default"

            return [FollowupAction(followup_action)]
        else:
            return []
