### Introduction

PH eReferral is provided in its initial DRAFT form to support the use of HL7<sup>&reg;</sup> FHIR<sup>&reg;&copy;</sup> in the Philippines context. It sets the minimum expectations on FHIR resources to support conformance and implementation in systems. This FHIR IG is for testing purposes only and not suitable for production systems.

<div style="padding: 1em; margin: 1.5em 0; border-left: 4px solid #f0ad4e; background: #fcf8e3;">
<strong>⚠ Experimental Fork</strong><br/>
This is a <strong>fork for experimental and display purposes only</strong>. It is not the authoritative source of the PH eReferral IG. This fork demonstrates three techniques that may be adopted upstream:

<ul>
<li><strong>Example-driven development</strong> — the IG is built around concrete FHIR resource examples derived from a real-world ANC scenario (patient Charity, clerk Abraham, nurse Jane), with every data-dictionary element traced to a working example instance.</li>
<li><strong>Automated versioning</strong> — the <code>main</code> branch always carries a <code>-draft</code> version (e.g. <code>0.2.0-draft</code>); release versions are derived from Git tags (<code>v0.1.0</code> → IG version <code>0.1.0</code>) so the source of truth is never ambiguous.</li>
<li><strong>Automated release</strong> — two GitHub Actions workflows publish the IG automatically: a CI lane deploys every push to <code>main</code> as a <a href="dev/">development preview</a>, while tagging a release publishes an immutable version to its own URL with history tracking.</li>
</ul>
</div>
