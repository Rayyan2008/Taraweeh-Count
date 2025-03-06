# main.py
from fastapi import FastAPI
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure

app = FastAPI()

# React Component for the Welcome Screen
@component
def WelcomeScreen(set_screen):
    def go_to_counter(event):
        set_screen("counter")  # Switch screen

    return html.div(
        {
            "style": {
                "textAlign": "center",
                "padding": "50px",
                "background": "linear-gradient(135deg, #0f0f23, #1a1a3d)",
                "color": "#FFD700",
                "minHeight": "100vh",
                "display": "flex",
                "flexDirection": "column",
                "alignItems": "center",
                "justifyContent": "center",
                "fontFamily": "Arial, sans-serif",
            }
        },
        html.h1("🤲 Assalamualaikum!"),
        html.p("Welcome to the Taraweeh Rakat Counter."),
        html.button(
            {"onClick": go_to_counter, "style": {"padding": "15px 25px", "fontSize": "22px", "background": "#FFD700"}},
            "Start"
        )
    )

# React Component for the Taraweeh Counter
@component
def TaraweehCounter(set_screen):
    rakat, set_rakat = use_state(0)

    def pray_rakat(event):
        if rakat < 20:
            set_rakat(rakat + 2)

    def reset_rakat(event):
        set_rakat(0)

    def go_home(event):
        set_screen("welcome")

    return html.div(
        {
            "style": {
                "textAlign": "center",
                "padding": "50px",
                "background": "linear-gradient(135deg, #0f0f23, #1a1a3d)",
                "color": "#FFD700",
                "minHeight": "100vh",
                "fontFamily": "Arial, sans-serif",
            }
        },
        html.h1("🌙 Taraweeh Rakat Counter"),
        html.p(f"Rakat: {rakat}/20"),
        html.button(
            {"onClick": pray_rakat, "style": {"padding": "15px", "background": "#FFD700"}},
            "✅ Pray 2 Rakats"
        ),
        html.button(
            {"onClick": reset_rakat, "style": {"padding": "15px", "background": "#FF6347"}},
            "🔄 Reset"
        ),
        html.button(
            {"onClick": go_home, "style": {"padding": "15px", "background": "#1E90FF"}},
            "🏠 Home"
        ),
    )

# Main App Component to switch between screens
@component
def App():
    screen, set_screen = use_state("welcome")
    return WelcomeScreen(set_screen) if screen == "welcome" else TaraweehCounter(set_screen)

# Configure FastAPI with React
configure(app, App)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

