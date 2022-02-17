# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/operator-framework/operator-sdk
%global goipath         github.com/operator-framework/operator-sdk
Version:                1.17.0

%gometa

%global common_description %{expand:
SDK for building Kubernetes applications. Provides high level APIs, useful
abstractions, and project scaffolding.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.MD README.md SECURITY.md code-of-\\\
                        conduct.md changelog/generated/v1.10.0.md\\\
                        changelog/generated/v1.11.0.md\\\
                        changelog/generated/v1.12.0.md\\\
                        changelog/generated/v1.13.0.md\\\
                        changelog/generated/v1.14.0.md\\\
                        changelog/generated/v1.15.0.md\\\
                        changelog/generated/v1.16.0.md\\\
                        changelog/generated/v1.17.0.md\\\
                        changelog/generated/v1.3.0.md\\\
                        changelog/generated/v1.4.0.md\\\
                        changelog/generated/v1.5.0.md\\\
                        changelog/generated/v1.6.0.md\\\
                        changelog/generated/v1.6.1.md\\\
                        changelog/generated/v1.7.0.md\\\
                        changelog/generated/v1.7.1.md\\\
                        changelog/generated/v1.8.0.md\\\
                        changelog/generated/v1.9.0.md proposals/README.md\\\
                        proposals/TEMPLATE.md proposals/ansible-helm-\\\
                        addapi.md proposals/ansible-operator-devex.md\\\
                        proposals/ansible-operator-status.md\\\
                        proposals/ansible-operator-testing.md\\\
                        proposals/ansible-operator.md proposals/automating-\\\
                        releases.md proposals/cli-ux-phase1.md\\\
                        proposals/helm-operator.md proposals/hugo-doc-\\\
                        build.md proposals/improve-csv-cli.md\\\
                        proposals/improved-scorecard-config.md\\\
                        proposals/kubebuilder-integration.md\\\
                        proposals/kubernetes-1.17.md proposals/leader-for-\\\
                        life.md proposals/metering-operator-metrics.md\\\
                        proposals/operator-testing-tool.md proposals/qa-\\\
                        samples-proposal.md proposals/scorecard-custom-\\\
                        tests-2.md proposals/scorecard-plugin-system.md\\\
                        proposals/sdk-code-annotations.md proposals/sdk-\\\
                        integration-with-olm.md proposals/tech-debt.md\\\
                        proposals/tls-utilities.md proposals/upstream-osdk-\\\
                        features-into-controller-runtime.md docs\\\
                        website/content/en/search.md\\\
                        website/content/en/community/_index.md docs

Name:           %{goname}
Release:        1%{?dist}
Summary:        SDK for building Kubernetes applications. Provides high level APIs, useful abstractions, and project scaffolding

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in images/scorecard-test-kuttl images/custom-scorecard-tests hack/generate/samples hack/generate/samples/molecule hack/generate/cli-doc release/changelog images/scorecard-test hack/generate/cncf-maintainers; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.MD README.md SECURITY.md code-of-conduct.md
%doc changelog/generated/v1.10.0.md changelog/generated/v1.11.0.md
%doc changelog/generated/v1.12.0.md changelog/generated/v1.13.0.md
%doc changelog/generated/v1.14.0.md changelog/generated/v1.15.0.md
%doc changelog/generated/v1.16.0.md changelog/generated/v1.17.0.md
%doc changelog/generated/v1.3.0.md changelog/generated/v1.4.0.md
%doc changelog/generated/v1.5.0.md changelog/generated/v1.6.0.md
%doc changelog/generated/v1.6.1.md changelog/generated/v1.7.0.md
%doc changelog/generated/v1.7.1.md changelog/generated/v1.8.0.md
%doc changelog/generated/v1.9.0.md proposals/README.md proposals/TEMPLATE.md
%doc proposals/ansible-helm-addapi.md proposals/ansible-operator-devex.md
%doc proposals/ansible-operator-status.md proposals/ansible-operator-testing.md
%doc proposals/ansible-operator.md proposals/automating-releases.md
%doc proposals/cli-ux-phase1.md proposals/helm-operator.md
%doc proposals/hugo-doc-build.md proposals/improve-csv-cli.md
%doc proposals/improved-scorecard-config.md proposals/kubebuilder-integration.md
%doc proposals/kubernetes-1.17.md proposals/leader-for-life.md
%doc proposals/metering-operator-metrics.md proposals/operator-testing-tool.md
%doc proposals/qa-samples-proposal.md proposals/scorecard-custom-tests-2.md
%doc proposals/scorecard-plugin-system.md proposals/sdk-code-annotations.md
%doc proposals/sdk-integration-with-olm.md proposals/tech-debt.md
%doc proposals/tls-utilities.md
%doc proposals/upstream-osdk-features-into-controller-runtime.md docs
%doc website/content/en/search.md website/content/en/community/_index.md docs
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Feb 14 2022 jesus m. rodriguez <jmrodri@gmail.com> - 1.17.0-1
- Initial package