from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, SwitchTo
from aiogram_dialog.widgets.input import TextInput
from bot.states.states import FeedbackSG
from bot.dialogs.start.getters import get_name
from bot.dialogs.feedback.handlers import accept_feedback


feedback_dialog = Dialog(
    Window(
        Format(
            "{name}, нажмите кнопку 'Отзыв', если у вас есть предложения\
            или пожелания по развитию проекта.\n\n Нажмите\
                кнопку 'Ошибка' если вы обнаружили ошибку в работе робота."
        ),
        SwitchTo(Const("Отзыв"), id="feedback", state=FeedbackSG.feedback),
        SwitchTo(Const("Ошибка"), id="bug_report", state=FeedbackSG.bug_report),
        state=FeedbackSG.start,
        getter=get_name,
    ),
    Window(
        Const("Напишите ваш отзыв"),
        TextInput(id="feedback", on_success=accept_feedback),
        state=FeedbackSG.feedback,
    ),
    Window(
        Const(
            "Подробно опишите ошибку в работе робота,\
               с которой вы столкнулись"
        ),
        TextInput(id="bug_report", on_success=accept_feedback),
        state=FeedbackSG.bug_report,
    ),
)
