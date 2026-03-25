import flet as ft
import random


def main(page: ft.Page):
    page.title = "🎲 Lucky Number"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f0f1a"
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- State ---
    secret = [random.randint(1, 100)]
    attempts = [0]
    max_attempts = 7
    game_over = [False]

    # --- UI Elements ---
    title = ft.Text(
        "🎲 Lucky Number",
        size=34,
        weight=ft.FontWeight.BOLD,
        color="#e040fb",
        text_align=ft.TextAlign.CENTER,
    )

    subtitle = ft.Text(
        "Devinez le nombre entre 1 et 100",
        size=14,
        color="#aaaacc",
        text_align=ft.TextAlign.CENTER,
    )

    attempts_text = ft.Text(
        f"Tentatives restantes : {max_attempts}",
        size=14,
        color="#80cbc4",
        text_align=ft.TextAlign.CENTER,
    )

    message = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.W_600,
        color="#ffffff",
        text_align=ft.TextAlign.CENTER,
    )

    hint = ft.Text(
        "",
        size=22,
        text_align=ft.TextAlign.CENTER,
    )

    input_field = ft.TextField(
        hint_text="Entre un nombre...",
        text_align=ft.TextAlign.CENTER,
        bgcolor="#1e1e2f",
        color="#ffffff",
        border_color="#e040fb",
        focused_border_color="#ea80fc",
        hint_style=ft.TextStyle(color="#555577"),
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=12,
    )

    guess_btn = ft.ElevatedButton(
        text="Deviner !",
        bgcolor="#e040fb",
        color="#ffffff",
        width=180,
        height=46,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    restart_btn = ft.ElevatedButton(
        text="Rejouer 🔄",
        bgcolor="#26c6da",
        color="#000000",
        width=180,
        height=46,
        visible=False,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    progress = ft.ProgressBar(
        value=1.0,
        bgcolor="#1e1e2f",
        color="#e040fb",
        width=260,
        height=8,
    )

    # --- Logic ---
    def check_guess(e):
        if game_over[0]:
            return

        raw = input_field.value.strip()
        if not raw.isdigit():
            message.value = "⚠️ Entre un nombre valide !"
            message.color = "#ffab40"
            hint.value = ""
            page.update()
            return

        guess = int(raw)
        if guess < 1 or guess > 100:
            message.value = "⚠️ Entre un nombre entre 1 et 100 !"
            message.color = "#ffab40"
            hint.value = ""
            page.update()
            return

        attempts[0] += 1
        remaining = max_attempts - attempts[0]
        progress.value = remaining / max_attempts

        if guess == secret[0]:
            message.value = f"🎉 Bravo ! C'était {secret[0]} !"
            message.color = "#69f0ae"
            hint.value = f"Trouvé en {attempts[0]} tentative(s) !"
            guess_btn.visible = False
            input_field.visible = False
            restart_btn.visible = True
            attempts_text.value = ""
            game_over[0] = True
        elif remaining == 0:
            message.value = f"💀 Perdu ! C'était {secret[0]}."
            message.color = "#ef5350"
            hint.value = "Tu manques de chance..."
            guess_btn.visible = False
            input_field.visible = False
            restart_btn.visible = True
            attempts_text.value = ""
            game_over[0] = True
        else:
            if guess < secret[0]:
                diff = secret[0] - guess
                if diff <= 5:
                    hint.value = "🔥 Très chaud ! Un peu plus haut..."
                    hint.color = "#ff7043"
                elif diff <= 20:
                    hint.value = "♨️ Chaud ! Monte encore..."
                    hint.color = "#ffab40"
                else:
                    hint.value = "❄️ Trop bas ! Monte !"
                    hint.color = "#64b5f6"
            else:
                diff = guess - secret[0]
                if diff <= 5:
                    hint.value = "🔥 Très chaud ! Un peu plus bas..."
                    hint.color = "#ff7043"
                elif diff <= 20:
                    hint.value = "♨️ Chaud ! Descends encore..."
                    hint.color = "#ffab40"
                else:
                    hint.value = "❄️ Trop haut ! Descends !"
                    hint.color = "#64b5f6"

            message.value = f"Pas encore..."
            message.color = "#aaaacc"
            attempts_text.value = f"Tentatives restantes : {remaining}"

        input_field.value = ""
        page.update()

    def restart(e):
        secret[0] = random.randint(1, 100)
        attempts[0] = 0
        game_over[0] = False
        message.value = ""
        hint.value = ""
        input_field.value = ""
        input_field.visible = True
        guess_btn.visible = True
        restart_btn.visible = False
        attempts_text.value = f"Tentatives restantes : {max_attempts}"
        progress.value = 1.0
        page.update()

    guess_btn.on_click = check_guess
    restart_btn.on_click = restart
    input_field.on_submit = check_guess

    # --- Layout ---
    page.add(
        ft.Column(
            [
                title,
                subtitle,
                ft.Container(height=16),
                progress,
                ft.Container(height=8),
                attempts_text,
                ft.Container(height=20),
                hint,
                ft.Container(height=6),
                message,
                ft.Container(height=20),
                input_field,
                ft.Container(height=14),
                guess_btn,
                restart_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
    )


ft.app(target=main)
