import os
import re

base_dir = '/Users/matheusrangel/Documents/SITE_MORAES'

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    idx_content = f.read()

with open(os.path.join(base_dir, 'portfolio.html'), 'r', encoding='utf-8') as f:
    port_content = f.read()

# Extract head
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', idx_content, re.DOTALL)
head = head_match.group(1)

# Extract body start
body_start = r'''
<body class="bg-background text-on-surface font-body selection:bg-primary selection:text-on-primary antialiased">
    <!-- Custom UI Overlays -->
    <div class="grain"></div>
    <div id="cursor-follower">
        <div id="cursor-dot"></div>
    </div>
    <div class="scroll-progress hidden md:block">
        <div class="progress-bar" id="progress"></div>
    </div>
    <div class="geometry-container">
        <div class="monolith-block block-1" id="m1"></div>
        <div class="monolith-block block-2" id="m2"></div>
    </div>
'''

nav_html = r'''
<!-- TopNavBar -->
<nav class="fixed top-6 w-[95%] lg:w-[92%] max-w-[1400px] left-1/2 -translate-x-1/2 z-50 glass-panel rounded-2xl transition-all duration-500">
    <div class="flex justify-between items-center px-8 lg:px-12 py-4 w-full mx-auto">
        <a href="index.html" class="interactive group flex items-center gap-3">
            <div class="relative w-12 h-12 flex items-center justify-center bg-white/5 rounded-xl border border-white/10 group-hover:border-primary/50 transition-all">
                <img src="LOGOS/customcolor/icon/customcolor_icon_transparent_background.png" alt="M" class="h-8 w-auto transition-transform duration-500 group-hover:scale-110" style="filter: brightness(0) invert(1);">
            </div>
            <div class="hidden sm:block">
                <div class="text-lg font-black tracking-tighter text-white leading-none">MORAES</div>
                <div class="text-[10px] font-bold text-primary tracking-[0.2em] mt-1">ENGENHARIA</div>
            </div>
        </a>

        <!-- Mobile Menu Button -->
        <button id="mobile-menu-btn" class="md:hidden text-white">
            <span class="material-symbols-outlined text-3xl">menu</span>
        </button>

        <div class="hidden md:flex items-center gap-8">
            <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] transition-colors nav-link-home" href="index.html">Home</a>
            <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] transition-colors nav-link-sobre" href="sobre.html">Sobre</a>
            <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] transition-colors nav-link-servicos" href="servicos.html">Serviços</a>
            <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] transition-colors nav-link-portfolio" href="portfolio.html">Portfólio</a>
            <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] transition-colors nav-link-contato" href="contato.html">Contato</a>
        </div>
        <a href="contato.html" class="hidden md:inline-flex interactive brushed-gold text-on-primary px-6 py-2 font-headline uppercase tracking-tighter text-sm font-bold scale-95 hover:scale-100 transition-transform hover:opacity-90">
            Fale Conosco
        </a>
    </div>

    <!-- Mobile Menu -->
    <div id="mobile-menu" class="hidden md:hidden absolute top-full mt-2 left-0 w-full bg-[#131313]/95 backdrop-blur-xl border border-white/10 rounded-b-md py-4 px-6 flex-col gap-4 shadow-xl">
        <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] nav-link-home" href="index.html">Home</a>
        <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] nav-link-sobre" href="sobre.html">Sobre</a>
        <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] nav-link-servicos" href="servicos.html">Serviços</a>
        <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] nav-link-portfolio" href="portfolio.html">Portfólio</a>
        <a class="font-headline uppercase tracking-tighter text-sm font-bold text-white hover:text-[#ffbe46] nav-link-contato" href="contato.html">Contato</a>
    </div>
</nav>

<script>
    document.getElementById('mobile-menu-btn')?.addEventListener('click', function() {
        const menu = document.getElementById('mobile-menu');
        if(menu) {
            menu.classList.toggle('hidden');
            menu.classList.toggle('flex');
        }
    });
</script>
'''

# Extract footer and script
footer_script_match = re.search(r'(<!-- Footer -->.*?)</body>', idx_content, re.DOTALL)
footer_script = footer_script_match.group(1)

# Fix links
footer_script = re.sub(r'href="index\.html#[a-z]+"', lambda m: f'href="{m.group(0).split("#")[1]}.html"', footer_script)
footer_script = re.sub(r'href="#([a-z]+)"', lambda m: f'href="{m.group(1)}.html"', footer_script)

def extract_section(section_id):
    pattern = r'(<section id="' + section_id + r'".*?</section>)'
    match = re.search(pattern, idx_content, re.DOTALL)
    if match: return match.group(1)
    return ""

sec_sobre = extract_section("sobre")
sec_servicos = extract_section("servicos")
sec_contato = extract_section("contato")

def wrap_page(title, content, nav_id):
    nav = nav_html.replace(f'text-white hover:text-[#ffbe46] transition-colors nav-link-{nav_id}', f'text-[#ffbe46] border-b-2 border-[#ffbe46] nav-link-{nav_id}')
    nav = nav.replace(f'text-white hover:text-[#ffbe46] nav-link-{nav_id}', f'text-[#ffbe46] nav-link-{nav_id}')
    page_head = head.replace('<title>MORAES - Engenharia e Construção Pesada</title>', f'<title>MORAES - {title}</title>')
    h = f"{page_head}\n{body_start}\n{nav}\n<main class='pt-32 pb-24 min-h-screen flex flex-col justify-center hero-gradient'>\n{content}\n</main>\n{footer_script}\n</body>\n</html>"
    return h.replace('href="index.html#contato"', 'href="contato.html"').replace('href="#contato"', 'href="contato.html"')

with open(os.path.join(base_dir, 'sobre.html'), 'w', encoding='utf-8') as f: f.write(wrap_page("Sobre Nós", sec_sobre, "sobre"))
with open(os.path.join(base_dir, 'servicos.html'), 'w', encoding='utf-8') as f: f.write(wrap_page("Nossos Serviços", sec_servicos, "servicos"))
with open(os.path.join(base_dir, 'contato.html'), 'w', encoding='utf-8') as f: f.write(wrap_page("Fale Conosco", sec_contato, "contato"))

sec_home = extract_section("home")
index_nav = nav_html.replace(f'text-white hover:text-[#ffbe46] transition-colors nav-link-home', f'text-[#ffbe46] border-b-2 border-[#ffbe46] nav-link-home')
index_nav = index_nav.replace(f'text-white hover:text-[#ffbe46] nav-link-home', f'text-[#ffbe46] nav-link-home')
file_index = f"{head}\n{body_start}\n{index_nav}\n<main class='min-h-screen'>\n{sec_home}\n</main>\n{footer_script}\n</body>\n</html>"
file_index = file_index.replace('href="index.html#contato"', 'href="contato.html"').replace('href="#contato"', 'href="contato.html"')
with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f: f.write(file_index)

port_nav = nav_html.replace(f'text-white hover:text-[#ffbe46] transition-colors nav-link-portfolio', f'text-[#ffbe46] border-b-2 border-[#ffbe46] nav-link-portfolio')
port_nav = port_nav.replace(f'text-white hover:text-[#ffbe46] nav-link-portfolio', f'text-[#ffbe46] nav-link-portfolio')
port_content = re.sub(r'<!-- TopNavBar -->.*?</script>', port_nav, port_content, flags=re.DOTALL)
port_content = re.sub(r'<!-- Footer -->.*?</body>', footer_script + '\n</body>', port_content, flags=re.DOTALL)
port_content = port_content.replace('href="index.html#contato"', 'href="contato.html"').replace('href="#contato"', 'href="contato.html"')
with open(os.path.join(base_dir, 'portfolio.html'), 'w', encoding='utf-8') as f: f.write(port_content)

print("Pages separated successfully!")
