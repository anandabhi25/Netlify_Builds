"""Build the original Portfolio Dot font. Requires fontTools; no network access.
Patterns are authored for this portfolio, not extracted from NDot or FontStruct.
Run: python3 tools/build_dot_font.py
"""
from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen

# Five columns, seven rows; lowercase deliberately shares the display capitals.
PATTERNS = {
'A':'01110 10001 10001 11111 10001 10001 10001',
'B':'11110 10001 10001 11110 10001 10001 11110',
'C':'01111 10000 10000 10000 10000 10000 01111',
'D':'11110 10001 10001 10001 10001 10001 11110',
'E':'11111 10000 10000 11110 10000 10000 11111',
'F':'11111 10000 10000 11110 10000 10000 10000',
'G':'01111 10000 10000 10111 10001 10001 01110',
'H':'10001 10001 10001 11111 10001 10001 10001',
'I':'11111 00100 00100 00100 00100 00100 11111',
'J':'00111 00010 00010 00010 10010 10010 01100',
'K':'10001 10010 10100 11000 10100 10010 10001',
'L':'10000 10000 10000 10000 10000 10000 11111',
'M':'10001 11011 10101 10101 10001 10001 10001',
'N':'10001 11001 11001 10101 10011 10011 10001',
'O':'01110 10001 10001 10001 10001 10001 01110',
'P':'11110 10001 10001 11110 10000 10000 10000',
'Q':'01110 10001 10001 10001 10101 10010 01101',
'R':'11110 10001 10001 11110 10100 10010 10001',
'S':'01111 10000 10000 01110 00001 00001 11110',
'T':'11111 00100 00100 00100 00100 00100 00100',
'U':'10001 10001 10001 10001 10001 10001 01110',
'V':'10001 10001 10001 10001 10001 01010 00100',
'W':'10001 10001 10001 10101 10101 10101 01010',
'X':'10001 10001 01010 00100 01010 10001 10001',
'Y':'10001 10001 01010 00100 00100 00100 00100',
'Z':'11111 00001 00010 00100 01000 10000 11111',
'0':'01110 10001 10011 10101 11001 10001 01110',
'1':'00100 01100 00100 00100 00100 00100 01110',
'2':'01110 10001 00001 00010 00100 01000 11111',
'3':'11110 00001 00001 01110 00001 00001 11110',
'4':'00010 00110 01010 10010 11111 00010 00010',
'5':'11111 10000 10000 11110 00001 00001 11110',
'6':'01110 10000 10000 11110 10001 10001 01110',
'7':'11111 00001 00010 00100 01000 01000 01000',
'8':'01110 10001 10001 01110 10001 10001 01110',
'9':'01110 10001 10001 01111 00001 00001 01110',
'.':'00000 00000 00000 00000 00000 00100 00100',
',':'00000 00000 00000 00000 00100 00100 01000',
':':'00000 00100 00100 00000 00100 00100 00000',
';':'00000 00100 00100 00000 00100 00100 01000',
'-':'00000 00000 00000 11111 00000 00000 00000',
'+':'00000 00100 00100 11111 00100 00100 00000',
'/':'00001 00001 00010 00100 01000 10000 10000',
'!':'00100 00100 00100 00100 00100 00000 00100',
'?':'01110 10001 00001 00010 00100 00000 00100',
'\'':'00100 00100 01000 00000 00000 00000 00000',
'"':'01010 01010 00000 00000 00000 00000 00000',
'(':'00010 00100 01000 01000 01000 00100 00010',
')':'01000 00100 00010 00010 00010 00100 01000',
'&':'01100 10010 10100 01000 10101 10010 01101',
'%':'11001 11010 00010 00100 01000 01011 10011',
'$':'00100 01111 10100 01110 00101 11110 00100',
'@':'01110 10001 10111 10101 10111 10000 01111',
'#':'01010 01010 11111 01010 11111 01010 01010',
'=':'00000 00000 11111 00000 11111 00000 00000',
'·':'00000 00000 00000 00100 00000 00000 00000',
'→':'00000 00100 00010 11111 00010 00100 00000',
'↓':'00000 00100 00100 00100 10101 01110 00100',
'↗':'00000 11111 00011 00101 01001 10000 00000',
}

def build():
    fb = FontBuilder(1000, isTTF=True)
    order=['.notdef','space']+[f'uni{ord(c):04X}' for c in PATTERNS]
    fb.setupGlyphOrder(order)
    cmap={ord(c):f'uni{ord(c):04X}' for c in PATTERNS}
    cmap.update({ord(c.lower()):cmap[ord(c)] for c in PATTERNS if c.isalpha()})
    cmap[32]='space';cmap[160]='space'
    for alias,source in [('−','-'),('–','-'),('—','-'),('’',"'"),('‘',"'"),('“','"'),('”','"')]:
        cmap[ord(alias)]=cmap[ord(source)]
    fb.setupCharacterMap(cmap)
    glyphs={}
    for name in order:
        pen=TTGlyphPen(None)
        if name not in ('.notdef','space'):
            char=chr(int(name[3:],16))
            for row,bits in enumerate(PATTERNS[char].split()):
                for col,bit in enumerate(bits):
                    if bit!='1':continue
                    x,y=90+col*110,90+(6-row)*110
                    r,k=37,20
                    pen.moveTo((x+r,y))
                    pen.qCurveTo((x+r,y+k),(x+k,y+r),(x,y+r))
                    pen.qCurveTo((x-k,y+r),(x-r,y+k),(x-r,y))
                    pen.qCurveTo((x-r,y-k),(x-k,y-r),(x,y-r))
                    pen.qCurveTo((x+k,y-r),(x+r,y-k),(x+r,y))
                    pen.closePath()
        glyphs[name]=pen.glyph()
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics({g:(620,53) if g!='space' else (310,0) for g in order})
    fb.setupHorizontalHeader(ascent=850,descent=-150)
    fb.setupNameTable({'familyName':'Portfolio Dot','styleName':'Regular','uniqueFontIdentifier':'PortfolioDot-1.0','fullName':'Portfolio Dot Regular','psName':'PortfolioDot-Regular','version':'Version 1.0','copyright':'Copyright 2026. Original portfolio dot-matrix design.','licenseDescription':'Released under the MIT License; see LICENSE-PortfolioDot.txt.'})
    fb.setupOS2(sTypoAscender=850,sTypoDescender=-150,usWinAscent=850,usWinDescent=150,usWeightClass=400)
    fb.setupPost();fb.setupMaxp()
    # Fixed timestamps make builds repeatable.
    fb.font['head'].created=fb.font['head'].modified=3876422400
    fb.font.recalcTimestamp=False
    fb.font.flavor='woff'
    out=Path(__file__).resolve().parents[1]/'fonts'/'PortfolioDot.woff'
    fb.save(out)
    print(f'Built {out.name}: {out.stat().st_size} bytes, {len(cmap)} characters')

if __name__=='__main__':build()
