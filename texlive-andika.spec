Name:		texlive-andika
Version:	64540
Release:	2
Summary:	andika fonts with support for all LaTeX engines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/andika
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/andika.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/andika.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Andika family of fonts designed by SIL
International especially for literacy use, taking into account
the needs of beginning readers. The focus is on clear,
easy-to-perceive letterforms that will not be readily confused
with one another.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/andika
%{_texmfdistdir}/fonts/vf/SIL/andika
%{_texmfdistdir}/fonts/type1/SIL/andika
%{_texmfdistdir}/fonts/truetype/SIL/andika
%{_texmfdistdir}/fonts/tfm/SIL/andika
%{_texmfdistdir}/fonts/map/dvips/andika
%{_texmfdistdir}/fonts/enc/dvips/andika
%doc %{_texmfdistdir}/doc/fonts/andika

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
