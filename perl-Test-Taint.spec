Summary: 	Tools to test taintedness
Name: 		perl-Test-Taint
Version: 	1.04
Release: 	9%{?dist}
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Test-Taint/
Source0: 	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 0.08

%description
Tainted data is data that comes from an unsafe source, such as the command
line, or, in the case of web apps, any GET or POST transactions. Read the 
perlsec man page for details on why tainted data is bad, and how to untaint
the data.

When you're writing unit tests for code that deals with tainted data, you'll
want to have a way to provide tainted data for your routines to handle, and 
easy ways to check and report on the taintedness of your data, in standard 
Test::More style.

%prep
%setup -q -n Test-Taint-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="${RPM_OPT_FLAGS}"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorarch}/Test
%{perl_vendorarch}/auto/Test
%{_mandir}/man3/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-7
- Rebuild for perl 5.10 (again)

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.04-6
- Rebuild for gcc43.

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-5
- rebuild for new perl

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.04-4
- Reflect perl-package split.
- Update license tag.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.04-3
- Mass rebuild.

* Mon Feb 20 2006 Ralf Corsepius <rc040203@freenet.de> - 1.04-2
- Rebuild.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 1.04-1
- FE submission.

* Sun Mar 20 2005 Ralf Corsepius <ralf@links2linux.de> - 1.04-0.pm.2
- Initial version.
