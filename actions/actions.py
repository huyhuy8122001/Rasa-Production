# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from test import get_dau_so


class ActionTest(Action):

    def name(self) -> Text:
        return "action_test"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        with open('data.json', 'r', encoding='utf-8') as db:
            data = json.load(db)

        entityValue = next(tracker.get_latest_entity_values(
            entity_type="danhmucsanpham"), None)

        print(entityValue)

        dauso = get_dau_so(data, entityValue)

        print(dauso)

        return [SlotSet("name", "Huy")]
