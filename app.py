import gradio as gr


def greeting(name):
    return f"Hello {name}"


bellamy_bowie = gr.Interface(greeting, "text", "text")
urly_murly_simmy = gr.Interface(lambda name: "Hello " + name, "text", "text")
ellis_cappy = gr.Interface(lambda name: "Hello " + name, "text", "text")

demo = gr.TabbedInterface(
    [bellamy_bowie, urly_murly_simmy, ellis_cappy],
    ["Bellamy Bowie", "Urly & Murly Simmy", "Ellis Cappy"])

demo.launch()
