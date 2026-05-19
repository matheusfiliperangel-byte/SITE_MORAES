import re

with open("contato.html", "r") as f:
    content = f.read()

replacements = {
    # TITLE
    '<title>Contato — Moraes Engenharia | Solicite uma Consultoria em SP e RJ</title>': '<title data-i18n="contact.title_tag">Contato — Moraes Engenharia | Solicite uma Consultoria em SP e RJ</title>',

    # NAV & FOOTER (same as before)
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="index.html">Home</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="index.html" data-i18n="nav.home">Home</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="sobre.html">Sobre</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="sobre.html" data-i18n="nav.about">Sobre</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="sobre.html">Sobre</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="sobre.html" data-i18n="nav.about">Sobre</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="servicos.html">Serviços</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="servicos.html" data-i18n="nav.services">Serviços</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="servicos.html">Serviços</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="servicos.html" data-i18n="nav.services">Serviços</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="portfolio.html">Portfólio</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="portfolio.html" data-i18n="nav.portfolio">Portfólio</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="portfolio.html">Portfólio</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="portfolio.html" data-i18n="nav.portfolio">Portfólio</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="contato.html">Contato</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-white/50 hover:text-white transition-all interactive" href="contato.html" data-i18n="nav.contact">Contato</a>',
    '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="contato.html">Contato</a>': '<a class="font-headline uppercase tracking-[0.3em] text-[11px] font-bold text-gold-premium transition-all interactive" href="contato.html" data-i18n="nav.contact">Contato</a>',
    '<span class="relative z-10 text-white">Fale Conosco</span>': '<span class="relative z-10 text-white" data-i18n="nav.cta">Fale Conosco</span>',

    '<a href="index.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4">Home</a>': '<a href="index.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4" data-i18n="nav.home">Home</a>',
    '<a href="sobre.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4">Sobre</a>': '<a href="sobre.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4" data-i18n="nav.about">Sobre</a>',
    '<a href="sobre.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4">Sobre</a>': '<a href="sobre.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4" data-i18n="nav.about">Sobre</a>',
    '<a href="servicos.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4">Serviços</a>': '<a href="servicos.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4" data-i18n="nav.services">Serviços</a>',
    '<a href="servicos.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4">Serviços</a>': '<a href="servicos.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4" data-i18n="nav.services">Serviços</a>',
    '<a href="portfolio.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4">Portfólio</a>': '<a href="portfolio.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4" data-i18n="nav.portfolio">Portfólio</a>',
    '<a href="contato.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4">Contato</a>': '<a href="contato.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-white hover:text-gold-premium font-bold interactive mt-4" data-i18n="nav.contact">Contato</a>',
    '<a href="contato.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4">Contato</a>': '<a href="contato.html" class="font-headline text-2xl uppercase tracking-[0.3em] text-gold-premium font-bold interactive mt-4" data-i18n="nav.contact">Contato</a>',
    
    '<p class="font-body text-[11px] tracking-[0.3em] uppercase text-white/30 max-w-xs leading-loose">\n                Construções comerciais de alto padrão em São Paulo e Rio de Janeiro.\n            </p>': '<p class="font-body text-[11px] tracking-[0.3em] uppercase text-white/30 max-w-xs leading-loose" data-i18n="footer.tagline">\n                Construções comerciais de alto padrão em São Paulo e Rio de Janeiro.\n            </p>',
    '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2">Navegação</h4>': '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2" data-i18n="footer.nav_title">Navegação</h4>',
    '<a href="index.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Início</a>': '<a href="index.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.home">Início</a>',
    '<a href="sobre.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Sobre</a>': '<a href="sobre.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.about">Sobre</a>',
    '<a href="servicos.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Serviços</a>': '<a href="servicos.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.services">Serviços</a>',
    '<a href="portfolio.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Obras</a>': '<a href="portfolio.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.portfolio">Obras</a>',
    '<a href="contato.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive">Contato</a>': '<a href="contato.html" class="text-white/40 hover:text-white font-headline text-[10px] tracking-[0.4em] uppercase transition-colors duration-300 interactive" data-i18n="footer.nav.contact">Contato</a>',
    '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2">Escritório Central</h4>': '<h4 class="text-gold-premium font-headline font-bold text-[11px] uppercase tracking-[0.5em] mb-2" data-i18n="footer.office_title">Escritório Central</h4>',
    '<p class="text-white/40 font-headline text-[10px] tracking-[0.4em] uppercase leading-loose">\n                Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo\n            </p>': '<p class="text-white/40 font-headline text-[10px] tracking-[0.4em] uppercase leading-loose" data-i18n="footer.office_address">\n                Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo\n            </p>',
    '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20">© 2026 Moraes Engenharia. Todos os direitos reservados.</p>': '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20" data-i18n="footer.copyright">© 2026 Moraes Engenharia. Todos os direitos reservados.</p>',
    '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20">CREA-SP 2884830 &nbsp;•&nbsp; CNPJ 47.457.237/0001-60</p>': '<p class="font-mono text-[9px] sm:text-[10px] tracking-[0.2em] uppercase text-white/20" data-i18n="footer.crea">CREA-SP 2884830 &nbsp;•&nbsp; CNPJ 47.457.237/0001-60</p>',

    # PAGE SPECIFIC - CONTATO
    '<div class="section-label mb-8">04 // PROPOSTA</div>': '<div class="section-label mb-8" data-i18n="contact.label">04 // PROPOSTA</div>',
    '<h2 class="font-headline text-5xl md:text-7xl font-black tracking-[-0.04em] uppercase text-white mb-16 leading-[1.0]">\n                        Acelere seu <br/> <span class="text-gold-premium italic font-light">Investimento</span>.\n                    </h2>': '<h2 class="font-headline text-5xl md:text-7xl font-black tracking-[-0.04em] uppercase text-white mb-16 leading-[1.0]" data-i18n="contact.title">\n                        Acelere seu <br/> <span class="text-gold-premium italic font-light">Investimento</span>.\n                    </h2>',
    '<p class="text-on-surface-variant text-lg md:text-xl mb-16 md:mb-24 max-w-md font-light leading-relaxed">\n                        Decisões rápidas constroem impérios. Solicite uma consultoria com nosso time técnico em SP ou RJ.\n                    </p>': '<p class="text-on-surface-variant text-lg md:text-xl mb-16 md:mb-24 max-w-md font-light leading-relaxed" data-i18n="contact.subtitle">\n                        Decisões rápidas constroem impérios. Solicite uma consultoria com nosso time técnico em SP ou RJ.\n                    </p>',
    '<h4 class="text-white font-headline font-bold uppercase text-[11px] tracking-[0.4em] mb-4">Sede Administrativa</h4>': '<h4 class="text-white font-headline font-bold uppercase text-[11px] tracking-[0.4em] mb-4" data-i18n="contact.office.title">Sede Administrativa</h4>',
    '<p class="text-on-surface-variant/70 text-sm tracking-widest font-light uppercase leading-loose">\n                                    Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo - SP\n                                </p>': '<p class="text-on-surface-variant/70 text-sm tracking-widest font-light uppercase leading-loose" data-i18n="contact.office.address">\n                                    Rua Boa Vista, 254 — Sala 1516<br>Centro Histórico, São Paulo - SP\n                                </p>',
    '<h4 class="text-white font-headline font-bold uppercase text-[11px] tracking-[0.4em] mb-4">Contato Corporativo</h4>': '<h4 class="text-white font-headline font-bold uppercase text-[11px] tracking-[0.4em] mb-4" data-i18n="contact.email.title">Contato Corporativo</h4>',
    '<span class="relative z-10 text-white border-l border-white/20 pl-6">Atendimento WhatsApp</span>': '<span class="relative z-10 text-white border-l border-white/20 pl-6" data-i18n="contact.whatsapp">Atendimento WhatsApp</span>',
    
    '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold">Nome Completo</label>': '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold" data-i18n="contact.form.name_label">Nome Completo</label>',
    'placeholder="SEU NOME"': 'placeholder="SEU NOME" data-i18n-placeholder="contact.form.name_placeholder"',
    
    '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold">E-mail Corporativo</label>': '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold" data-i18n="contact.form.email_label">E-mail Corporativo</label>',
    'placeholder="SEU EMAIL"': 'placeholder="SEU EMAIL" data-i18n-placeholder="contact.form.email_placeholder"',
    
    '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold">Mensagem Técnica</label>': '<label class="font-mono text-[11px] uppercase tracking-[0.4em] text-gold-premium font-bold" data-i18n="contact.form.message_label">Mensagem Técnica</label>',
    'placeholder="ESCOPO DO PROJETO..."': 'placeholder="ESCOPO DO PROJETO..." data-i18n-placeholder="contact.form.message_placeholder"',
    
    'Solicitar Proposta\n                        </button>': '<span data-i18n="contact.form.submit">Solicitar Proposta</span>\n                        </button>',
    '<h3 class="font-headline font-bold text-white text-2xl md:text-3xl uppercase tracking-[0.2em] mb-4">Proposta Enviada</h3>': '<h3 class="font-headline font-bold text-white text-2xl md:text-3xl uppercase tracking-[0.2em] mb-4" data-i18n="contact.form.success.title">Proposta Enviada</h3>',
    '<p class="text-white/50 font-body text-sm md:text-base tracking-wider max-w-sm mx-auto leading-relaxed">Nossa equipe técnica retornará em até 24h úteis.</p>': '<p class="text-white/50 font-body text-sm md:text-base tracking-wider max-w-sm mx-auto leading-relaxed" data-i18n="contact.form.success.desc">Nossa equipe técnica retornará em até 24h úteis.</p>'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Toggle button
if 'class="lang-toggle' not in content:
    toggle_html = '<button class="lang-toggle font-headline uppercase tracking-[0.2em] text-[10px] font-bold text-white/70 hover:text-gold-premium transition-all interactive border border-white/15 hover:border-gold-premium/50 px-3 py-2 mr-4 lg:ml-8" type="button">中文</button>'
    content = content.replace('<button class="lg:hidden', f'{toggle_html}\n        <button class="lg:hidden')

# Script
if '<script src="translations.js"></script>' not in content:
    content = content.replace('</body>', '<script src="translations.js"></script>\n</body>')
    
# Change JS loading state translation
content = content.replace("submitBtn.textContent = 'ENVIANDO...';", "submitBtn.textContent = window.MoraesI18n ? (window.MoraesI18n.getLang() === 'zh' ? '发送中...' : 'ENVIANDO...') : 'ENVIANDO...';")

with open("contato.html", "w") as f:
    f.write(content)

print("contato.html updated")
