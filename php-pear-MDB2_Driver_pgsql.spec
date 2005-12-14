%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_pgsql
%define		_status		beta
%define		_pearname	MDB2_Driver_pgsql

Summary:	%{_pearname} - pgsql MDB2 driver
Summary(pl):	%{_pearname} - sterownik pgsql dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f2677312c9bf534ba7d984c75a83c2c6
URL:		http://pear.php.net/package/MDB2_Driver_pgsql/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.3.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0beta6
Requires:	php-pgsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PostGreSQL MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik PostGreSQL dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/pgsql.php
%{php_pear_dir}/MDB2/Driver/Manager/pgsql.php
%{php_pear_dir}/MDB2/Driver/Native/pgsql.php
%{php_pear_dir}/MDB2/Driver/Reverse/pgsql.php
%{php_pear_dir}/MDB2/Driver/pgsql.php
%{php_pear_dir}/package_pgsql.php
