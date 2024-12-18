from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Cancel, SwitchTo
from aiogram_dialog.widgets.input import TextInput
from bot.states.states import FeedbackSG
from bot.dialogs.start.getters import getter_of_start_data
from bot.dialogs.feedback.handlers import (
    accept_feedback,
    move_to_bug_report,
    move_to_feedback,
)


feedback_dialog = Dialog(
    Window(
        Format(
            "{name}, нажмите кнопку 'Отзыв', если у вас есть предложения "
            "или пожелания по развитию проекта.\n\nНажмите кнопку "
            "'Ошибка если вы обнаружили ошибку в работе робота."
        ),
        Button(Const("Отзыв"), id="feedback", on_click=move_to_feedback),
        Button(Const("Ошибка"), id="bug_report", on_click=move_to_bug_report),
        Cancel(Const("« Назад"), id="cancel"),
        state=FeedbackSG.start,
        getter=getter_of_start_data,
    ),
    Window(
        Const("Напишите ваш отзыв:"),
        TextInput(id="feedback", on_success=accept_feedback),
        SwitchTo(Const("« Назад"), id="to_start", state=FeedbackSG.start),
        state=FeedbackSG.feedback,
    ),
    Window(
        Const("Подробно опишите ошибку в работе робота, с которой вы столкнулись:"),
        TextInput(id="bug_report", on_success=accept_feedback),
        SwitchTo(Const("« Назад"), id="to_start", state=FeedbackSG.start),
        state=FeedbackSG.bug_report,
    ),
)
