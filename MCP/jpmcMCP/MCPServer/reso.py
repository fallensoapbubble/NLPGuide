from agent import mcp


# 4. Define Resources (The Context)

@mcp.resource("sdlc://architecture/guidelines")
def architecture_guidelines() -> str:
    """
    Returns the firm's strict architectural guidelines for AI Agents.
    The LLM reads this to ensure generated code is compliant.
    """
    return """
    === JPMC ARCHITECTURE STANDARDS ===
    1. CONCURRENCY: All I/O bound operations must be Async (Python asyncio).
    2. SECURITY: No PII (Personally Identifiable Information) in stdout/stderr.
    3. INFRASTRUCTURE: All Python services must be containerized (Docker) and deployed on EKS.
    4. OBSERVABILITY: Use OpenTelemetry for tracing.
    """

@mcp.resource("jpmc://security/policies")
def security_policies() -> str:
    """
    Returns JPMC's strict security policies for AI Agents.
    """
    return """
    === JPMC SECURITY POLICIES ===
    1. AUTHENTICATION: All services must use OAuth2.0 with short-lived tokens.
    2. AUTHORIZATION: Role-Based Access Control (RBAC) enforced at API gateway level.
    3. DATA ENCRYPTION: TLS 1.3 required for all traffic; AES-256 for data at rest.
    4. SECRETS MANAGEMENT: All secrets stored in HashiCorp Vault; never hardcoded in code or configs.
    5. AUDIT & LOGGING: All access logged; logs retained for a minimum of 90 days.
    6. SECURE CODING: No PII in stdout/stderr; sanitize all inputs to prevent injection attacks.
    7. IMAGE SCANNING: All container images scanned for vulnerabilities before deployment.
    8. PATCHING: Critical security patches applied within 48 hours of release.
    9. NETWORK SECURITY: Services must run inside private VPCs; ingress controlled via service mesh.
    10. COMPLIANCE: All systems must adhere to SOX, PCI-DSS, and GDPR where applicable.
    """



@mcp.resource("sdlc://coding/standards")
def coding_standards() -> str:
    """
    Returns the firm's Python coding standards for AI Agents.
    """
    return """
    === JPMC CODING STANDARDS ===
    1. STYLE: Follow PEP8 with flake8 enforcement.
    2. TYPE SAFETY: Use type hints and mypy checks.
    3. ERROR HANDLING: Explicit exception handling; no bare except.
    4. DEPENDENCY MANAGEMENT: Use poetry/requirements.txt with pinned versions.
    5. DOCUMENTATION: Docstrings required for all public functions/classes.
    """

@mcp.resource("docker://deployment/practices")
def docker_deployment_practices() -> str:
    """
    Returns the firm's Docker deployment practices for AI Agents.
    """
    return """
    === JPMC DOCKER DEPLOYMENT PRACTICES ===
    1. BASE IMAGE: Use only approved lightweight base images (e.g., python:3.11-slim).
    2. SECURITY: Run containers as non-root; apply image scanning (Trivy/Clair).
    3. CONFIGURATION: Environment variables injected via Kubernetes ConfigMaps/Secrets.
    4. NETWORKING: Containers must expose only required ports; use service mesh for traffic control.
    5. STORAGE: Containers must be stateless; persistent data handled via EKS volumes.
    6. BUILD: Dockerfiles must be multi-stage builds to minimize image size.
    7. VERSIONING: Images tagged with semantic versioning and Git commit SHA.
    8. DEPLOYMENT: All services deployed via Helm charts on EKS.
    9. MONITORING: Sidecar containers for logging/tracing integrated with OpenTelemetry.
    10. COMPLIANCE: Images pulled only from internal artifact registry; no public registry usage.
    """



