import re

with open("index.html", "r") as f:
    content = f.read()

# Add data-i18n to footer tags
replacements = {
    '<p class="font-body text-[11px] tracking-[0.3em] uppercase text-white/30 max-w-xs leading-loose">': '<p class="font-body text-[11px] tracking-[0.3em] uppercase text-white/30 max-w-xs leading-loose" data-i18n="footer.tagline">',
    
    '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2">Navegação</h4>': '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2" data-i18n="footer.nav_title">Navegação</h4>',
    
    '<a href="index.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Início</a>': '<a href="index.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.home">Início</a>',
    
    '<a href="sobre.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Sobre</a>': '<a href="sobre.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.about">Sobre</a>',
    
    '<a href="servicos.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Serviços</a>': '<a href="servicos.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.services">Serviços</a>',
    
    '<a href="portfolio.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Obras</a>': '<a href="portfolio.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.portfolio">Obras</a>',
    
    '<a href="contato.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Contato</a>': '<a href="contato.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.contact">Contato</a>',
    
    '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2">Escritório Central</h4>': '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2" data-i18n="footer.office_title">Escritório Central</h4>',
    
    '<p class="text-white/40 font-headline text-[10px] tracking-[0.4em] uppercase leading-loose">\n                Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo\n            </p>': '<p class="text-white/40 font-headline text-[10px] tracking-[0.4em] uppercase leading-loose" data-i18n="footer.office_address">\n                Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo\n            </p>',
    
    '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20">© 2026 Moraes Engenharia. Todos os direitos reservados.</p>': '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20" data-i18n="footer.copyright">© 2026 Moraes Engenharia. Todos os direitos reservados.</p>',
    
    '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20">CREA-SP 2884830 &nbsp;•&nbsp; CNPJ 47.457.237/0001-60</p>': '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20" data-i18n="footer.crea">CREA-SP 2884830 &nbsp;•&nbsp; CNPJ 47.457.237/0001-60</p>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Add script at the end before </body>
if '<script src="translations.js"></script>' not in content:
    content = content.replace('</body>', '<script src="translations.js"></script>\n</body>')

with open("index.html", "w") as f:
    f.write(content)

print("index.html updated")
