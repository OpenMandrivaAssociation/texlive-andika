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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Andika family of fonts designed by SIL International especially for
literacy use, taking into account the needs of beginning readers. The
focus is on clear, easy-to-perceive letterforms that will not be readily
confused with one another.

