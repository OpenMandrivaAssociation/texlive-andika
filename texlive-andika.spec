%global tl_name andika
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.101
Release:	%{tl_revision}.1
Summary:	andika fonts with support for all LaTeX engines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/andika
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/andika.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/andika.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Andika family of fonts designed by SIL International especially for
literacy use, taking into account the needs of beginning readers. The
focus is on clear, easy-to-perceive letterforms that will not be readily
confused with one another.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/andika
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/SIL
%dir %{_datadir}/texmf-dist/fonts/truetype/SIL
%dir %{_datadir}/texmf-dist/fonts/type1/SIL
%dir %{_datadir}/texmf-dist/fonts/vf/SIL
%dir %{_datadir}/texmf-dist/tex/latex/andika
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/andika
%dir %{_datadir}/texmf-dist/fonts/map/dvips/andika
%dir %{_datadir}/texmf-dist/fonts/tfm/SIL/andika
%dir %{_datadir}/texmf-dist/fonts/truetype/SIL/andika
%dir %{_datadir}/texmf-dist/fonts/type1/SIL/andika
%dir %{_datadir}/texmf-dist/fonts/vf/SIL/andika
%doc %{_datadir}/texmf-dist/doc/fonts/andika/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/andika/README
%doc %{_datadir}/texmf-dist/doc/fonts/andika/about.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/about.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/andika-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/andika-samples.tex
%doc %{_datadir}/texmf-dist/doc/fonts/andika/announcement.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/charset.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/charset.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/design.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/design.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/developer.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/developer.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/faq.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/faq.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/features.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/features.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/history.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/history.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/index.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/index.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/resources.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/resources.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/support.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/support.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/andika/versions.md
%doc %{_datadir}/texmf-dist/doc/fonts/andika/versions.pdf
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_4x6wej.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_5kj227.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_d7tkvq.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_fh3q3k.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_fryoln.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_gn36ar.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_hrgzjy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_k2qdsf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_lqpsni.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_q2mpm3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_slnzzz.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_xvqrq2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_zn43lu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/andika/a_zvjtl6.enc
%{_datadir}/texmf-dist/fonts/map/dvips/andika/andika.map
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2a--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2b--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2c--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-sc-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2a--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2b--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2c--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-sc-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-BoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2a--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2b--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2c--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-sc-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2a--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2b--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2c--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-sc-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-t2a.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-t2b.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-t2c.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/SIL/andika/andk-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/truetype/SIL/andika/Andika-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/SIL/andika/Andika-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/SIL/andika/Andika-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/SIL/andika/Andika-Regular.ttf
%{_datadir}/texmf-dist/fonts/type1/SIL/andika/andk-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/SIL/andika/andk-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/SIL/andika/andk-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/SIL/andika/andk-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-t2a.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-t2b.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-sc-t2c.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-t2a.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-t2b.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-sc-t2c.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-BoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-t2a.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-t2b.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-sc-t2c.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-t2a.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-t2b.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-sc-t2c.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/SIL/andika/andk-tlf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/andika/LY1andk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/OT1andk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/T1andk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/T2Aandk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/T2Bandk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/T2Candk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/TS1andk-TLF.fd
%{_datadir}/texmf-dist/tex/latex/andika/andika.sty
