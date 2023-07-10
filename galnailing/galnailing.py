"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pandas as pd
import pynecone as pc
from PIL import Image
from PIL import ImageTk
from typing import List

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


# storage table rows
class storagetable:
    class row1:
        nail1 = pc.link("nail 1", href="/nail1", border="0.1em solid", color = "blue", padding="0.3em")
        o0001 = pc.hstack(
                pc.image(src = "testimg001.jpeg",width="100px",),
                pc.image(src = "testnail.jpeg",width="100px",)
        )
    class row2:
        nail_fairy = pc.link("nail fairy", href="/nail1", border="0.1em solid", color = "blue", padding="0.3em")
        c0002 = pc.hstack(
                pc.image(src = "testimg001.jpeg",width="100px",),
                pc.image(src = "testnail.jpeg",width="100px",)
        )
    class row3:
        french_nail = pc.link("french nail", href="/nail1", border="0.1em solid", color = "blue", padding="0.3em")
        m0001 = pc.hstack(
                pc.image(src = "testimg001.jpeg",width="100px",),
                pc.image(src = "testnail.jpeg",width="100px",)
        )



dict = {
        'Name': ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths': [87, 91, 97, 95],
        'Science': [83, 99, 84, 76],
        'Image': ['BTTTT~~adfads~~~','TBD','TBD','TBD']
        }

df = pd.DataFrame(dict)

df.iloc[0, 2]=df.iloc[0][1]

class database:
    xtable_head = ['NUMBER','NAME','LOCATION','NUM_XS','NUM_AVAIL_XS','PRICE','IMAGE']
    xtable_data = [
        ['O0001', storagetable.row1.nail1, 'Ottawa', 1, 2, '$30', storagetable.row1.o0001],
        ['C0002', storagetable.row2.nail_fairy, 'Chongqing', 3, 3, '$30', storagetable.row2.c0002],
        ['M0001', storagetable.row3.french_nail, 'Montreal', 1, 1, '$25', storagetable.row3.m0001]
    ]

# all Pages
class pages:
    mainpage = pc.link(
        "How to use",
        href="/",
        border="0.2em solid",
        padding="0.6em",
        border_radius="0.6em",
        button=True,
        _hover={
            "color": pc.color_mode_cond(
                light="rgb(107,99,246)",
                dark="rgb(179, 175, 255)",
            )
        },
    )

    breadcrumb = pc.breadcrumb(
        pc.breadcrumb_item(
            pc.breadcrumb_link("HOME", href='/', )
        ),
        pc.breadcrumb_item(
            pc.breadcrumb_link("nail1", href='/nail1', )
        ),
        separator="->",
        color="rgb(107,99,246)",
        # is_current_page = True,
    )


"""
# main page
def index() -> pc.Component:
    return pc.fragment(
        #pc.color_mode_button(pc.color_mode_icon(), float="right"),

        pc.vstack(
            pc.image(src="testnail.jpeg"),
            pc.heading("Welcome to Little Tail!", font_size="2em"),
            pc.box("Coding in ", pc.code(filename, font_size="1em")),
            pc.link(
                "Going to Nail storage",
                href="/storage-page",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": pc.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),

            font_size="2em",
            padding_top="1%",
            padding_bottom="5%",
        ),
    )

# page level 2 for nail general description
def storage():
    return pc.fragment(
        pc.hstack(
            pc.text(" "),
            pages.mainpage,
            pages.breadcrumb,
            spacing="44em",
            padding_top="1%",
        ),
        pc.vstack(
            pc.heading("Welcome to Little Tail Storage!", font_size="2em"),
            pc.data_table(
                data=df
            ),
            pc.text("Here is the Storage Page"),
                pc.table_container(
                    pc.table(
                        pc.thead(
                            pc.tr(*[pc.th(column) for column in database.xtable_head])
                        ),
                        pc.tbody(
                            *[
                                pc.tr(*[pc.td(item) for item in row])
                                for row in database.xtable_data
                            ]),
                        variant="striped",
                        # color_scheme="teal",
                    )
                ),

            padding_top="10%",
        )
    )



"""

# main page
def index() -> pc.Component:
    return pc.fragment(
        pc.hstack(
            pc.text(" "),
            pages.mainpage,
            #pages.breadcrumb,
            spacing="94em",
            padding_top="1%",
        ),
        pc.vstack(
            pc.heading("Welcome to Little Tail !", font_size="8em"),
            pc.image(src="mainp_nail.jpg"),
            padding_top="5%",
            padding_bottom="11%",
        ),
        pc.vstack(
            pc.text("Storage Table:", font_size="3em"),
            pc.table_container(
                pc.table(
                    pc.thead(
                        pc.tr(*[pc.th(column) for column in database.xtable_head])
                    ),
                    pc.tbody(
                        *[
                            pc.tr(*[pc.td(item) for item in row])
                            for row in database.xtable_data
                        ]),
                    variant="striped",
                    # color_scheme="teal",
                )
            ),
        ),
        padding_top="3%",
    )




# page level 3: nail1
def nail1():
    return pc.fragment(
        pc.hstack(
            pc.text(" "),
            pages.mainpage,
            pages.breadcrumb,
            spacing="44em",
            padding_top="1%",
        ),
        pc.hstack(
            pc.text(" "),
            pc.heading("Nail 1!", font_size="3em"),
            spacing="20em",
            padding_top="1%",
        ),

    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route="/")
app.add_page(nail1, route="/nail1")
app.compile()
