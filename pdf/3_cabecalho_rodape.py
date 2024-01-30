from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("dev aprender.png", x=1.2, h=0.8)
        #self.ln(0.1)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 12)
        self.cell(w=0, h=1, txt='Dev Aprender',
                  align='l', new_x='LMARGIN', new_y='NEXT')
        # Performing a line break:
        self.ln(0.1)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-1.5)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(w=0, h=1, txt=f"Página {self.page_no()}/{{nb}}", align="C")


pdf = PDF(unit='cm')
pdf.add_page()
pdf.set_font("Times", size=12)
# for i in range(1, 41):
#     pdf.cell(
#         w=0, h=1, txt=f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
texto_longo = '''I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. North America should be called Russia since people are always moving so fast. Gralitica. Twitter is the rice of social media. If you wake up with a giant zit, you are really facing your fears when you look in the mirror. If you wake up with a giant zit, you are really facing your fears when you look in the mirror.

Do we make money or does money make us? Chezwich. You say potatoe, I say starchy carbs. Most streets are two-way streets...why does that make love so special?. I don't need a big house, just a two-floor condo - you could say I have lofty expectations. A tagline for a car company that prides itself on its morals and ethics: Take the High Road.

A tagline for a special highway that is easy to navigate while under the influence of drugs: Take the High Road. I don't need a big house, just a two-floor condo - you could say I have lofty expectations. Logan Ipsum will loop at some point. Most streets are two-way streets...why does that make love so special?. I'm in a band that does Metallica covers with our private parts - it's called Myphallica. Petrovache.

For the name of an act as serious as killing someone, assassination literally translates to buttbuttination. Smiling could easily be misinterpreted for showing your teeth to someone because they said something that made you happy. North America should be called Russia since people are always moving so fast. Gralitica. INjuries always keep you OUT of things. Visticula. Rumour has it targeted online advertising was developed because the internet was upset that you could read it but it couldn't read you. Trepidelicious.

Pantone is a colour but also the singular version of pants. This is a true fact: I never had a fear of heights until I fell off a roof. We need more werkin and less twerkin if you ask me. Balooby. Logan Ipsum will loop at some point. North America should be called Russia since people are always moving so fast. Gralitica.

A tagline for a car company that prides itself on its morals and ethics: Take the High Road. Twitter is the rice of social media. If you were a member of the Bloods and became paralyzed do you then become a member of the Crips?. If you work for an ad agency and getting paid for it aren't you the one who is being influenced by advertising?. Curling is the best sport named after something you do to your hair.

I'm still upset that Tie Domi didn't name his child Tyson. You know the Grammys are a joke when Future doesn't win Best Everything. If a dog and cat had a baby together that grew up and worked a desk job he'd be a Cog in the machine. I'm in a band that does Metallica covers with our private parts - it's called Myphallica. Petrovache. I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness.

I have a moral code, but I haven't figured out how to read it yet. We need more werkin and less twerkin if you ask me. Balooby. I'm still upset that Tie Domi didn't name his child Tyson. To Catch A Predator would have been a great name for a Steve Irwin show. Mintslavicia. For the name of an act as serious as killing someone, assassination literally translates to buttbuttination.

I'm the only person in the world with my name. Do we make money or does money make us? Chezwich. If you wake up with a giant zit, you are really facing your fears when you look in the mirror. I have a moral code, but I haven't figured out how to read it yet. INjuries always keep you OUT of things. Visticula.

I have a moral code, but I haven't figured out how to read it yet. If a dog and cat had a baby together that grew up and worked a desk job he'd be a Cog in the machine. If you work for an ad agency and getting paid for it aren't you the one who is being influenced by advertising?. If a dog and cat had a baby together that grew up and worked a desk job he'd be a Cog in the machine. I bet most serial killers play the drums.

Twitter is the rice of social media. A tagline for a car company that prides itself on its morals and ethics: Take the High Road. Cemeteries are just garbage dumps filled with humans. Are there Out-of-Stock photos? Gafuffle. We need more werkin and less twerkin if you ask me. Balooby.

I think of a lot of good ideas when going to the bathroom - I guess I have a real stream of consciousness. I bet most serial killers play the drums. A tagline for a car company that prides itself on its morals and ethics: Take the High Road. If Fantasy Hockey actually lived up to its name, every team would have Henrik Lundqvist and Joffrey Lupul on it. A tagline for an airline: Take the High Road.

Most streets are two-way streets...why does that make love so special?. Smiling could easily be misinterpreted for showing your teeth to someone because they said something that made you happy. You should "listen to my mixtape" (check out the rest of my portfolio). I'm the only person in the world with my name. A tagline for a car company that prides itself on its morals and ethics: Take the High Road.

You say potatoe, I say starchy carbs. Logan Broger is "amazing" and a "wonderful boy" according to Logan's mom. Felinamiss. You know the Grammys are a joke when Future doesn't win Best Everything. You should "listen to my mixtape" (check out the rest of my portfolio). You say potatoe, I say starchy carbs.

Do we make money or does money make us? Chezwich. We say we are walking the dog, but the dog always leads. Twitter is the rice of social media. A tagline for a special highway that is easy to navigate while under the influence of drugs: Take the High Road. I have a moral code, but I haven't figured out how to read it yet.'''
pdf.multi_cell(w=0,h=1,txt=texto_longo,align='j',new_x='LMARGIN',new_y='NEXT')
pdf.output("demo.pdf")