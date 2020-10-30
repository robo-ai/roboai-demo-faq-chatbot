import pytest

from rasa.core.domain import Domain
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from bot.actions.action_default_fallback import ActionDefaultFallback


@pytest.fixture
def action_default_fallback():
    return ActionDefaultFallback()


@pytest.fixture
def default_domain():
    return Domain(
        intents={},
        entities=[],
        slots=[],
        templates={},
        action_names=["utter_welcome", ],
        form_names=[],
    )


@pytest.fixture
def default_dispatcher():
    return CollectingDispatcher()


def test_name(action_default_fallback):
    name = action_default_fallback.name()

    assert name == "action_default_fallback"


def test_run(action_default_fallback, default_dispatcher, default_domain):

    default_tracker = Tracker(
        sender_id="c9er45css2923",
        slots={},
        latest_message={},
        events=[],
        paused=False,
        followup_action=None,
        active_form=None,
        latest_action_name=None,
    )

    result = action_default_fallback.run(default_dispatcher, default_tracker, default_domain)
    print(result)
    event = result[0]['event']
    assert event == 'rewind'
