%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_pgsql
%define		_status		stable
%define		_pearname	MDB2_Driver_pgsql

Summary:	%{_pearname} - pgsql MDB2 driver
Summary(pl):	%{_pearname} - sterownik pgsql dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	90e3ba36905075f49a3c6425e8d5cea9
URL:		http://pear.php.net/package/MDB2_Driver_pgsql/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.0.3
Requires:	php-pear-PEAR-core >= 1:1.0b1
Requires:	php-pgsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PostgreSQL MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik PostgreSQL dla MDB2.

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
%{php_pear_dir}/MDB2/Driver/Function/pgsql.php
