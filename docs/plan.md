# Pit Duncan: Refactoring & Architecture Plan

This document outlines the step-by-step strategy to transition the Pit Duncan application from its current Streamlit mockup into a fully-fledged, secure, and modern web application using **FastAPI**, **MongoDB**, and **Angular + Tailwind CSS**.

## Core Strategy: The Iterative Loop
To ensure perfect alignment with requirements, every phase will follow a strict cycle:
1. **Plan**: Outline the architectural scope and requirements for the phase.
2. **Ask**: Present the plan to stakeholders for feedback, clarification, and approval.
3. **Implement**: Execute the code generation, testing, and integration.
4. *(Repeat until complete)*

---

## Step 0: The Clean Slate
- **Action**: Delete the current `src/` folder and `main.py`.
- **Action**: Initialize the new repository architecture with clear separation of concerns (e.g., `backend/` for FastAPI, `frontend/` for Angular).

---

## Phase 1: Infrastructure & Secrets Management
- **Plan**: Define the environment configuration strategy to secure sensitive data (MongoDB connection strings, JWT secrets).
- **Implement**: Set up `.env` loaders in Python (e.g., `pydantic-settings`), configure `.gitignore`, and ensure no secrets are hardcoded in the repository. *(This fulfills the low-priority goal of learning AI secrets management early on).*

---

## Phase 2: Database Schema Expansion & Unification
- **Plan**: Map the existing MongoDB schema (`migration_report.md`) to strict backend models (using Pydantic or Beanie) and add new architectural requirements.
- **Implement**:
  - **New Collection (`DocumentRegistry` / `Secrets`)**: A centralized ledger to track all produced PDFs (Prescriptions, Invoices, Tickets).
  - **State Tracking**: Add `is_used` or `status` fields to prescriptions to ensure a medicine can only be purchased once per prescription.
  - **Unified Users**: Standardize the `usuarios` collection to use strict Role-Based Access Control (`role: "ADMIN" | "DOCTOR" | "PATIENT"`).

---

## Phase 3: Backend Authentication & RBAC
- **Plan**: Design the unified login workflow and security dependencies.
- **Implement**:
  - Build the login endpoint to issue secure JSON Web Tokens (JWT).
  - Create FastAPI dependencies (the equivalent of Java's `@RolesAllowed`) to aggressively protect routes (`@require_role("ADMIN")`).

---

## Phase 4: Secure Document Generation & Validation (Steganography)
- **Plan**: Design the PDF generation engine and the anti-forgery validation mechanism.
- **Implement**:
  - Centralize all PDF generation into a single, scalable service to unify the document aesthetics.
  - **Functional Steganography**: Embed a unique cryptographic hash or an invisible, encrypted text block into every generated PDF. This hash maps directly to the `DocumentRegistry` collection.
  - **Validation Endpoint**: Build an endpoint that accepts PDF uploads (e.g., when a patient buys restricted medicine), extracts the hidden steganographic key, queries the database, and validates whether the prescription is authentic, belongs to the patient, and hasn't been redeemed yet.

---

## Phase 5: Core API Endpoints (CRUD)
- **Plan**: Map out the RESTful routes required by the frontend.
- **Implement**:
  - `GET /api/inventory`, `POST /api/inventory` (Admin)
  - `GET /api/patients`, `POST /api/patients` (Doctors)
  - `POST /api/appointments` (Public & Doctors)

---

## Phase 6: Frontend Foundation (Angular + Tailwind CSS)
- **Plan**: Establish the design system and application shell.
- **Implement**:
  - Setup the Angular workspace.
  - Configure Tailwind CSS with a curated, appealing, and highly professional color palette.
  - **UX Unification**: Build highly reusable, unified UI components (e.g., standardized datalists with search, unified data tables, standardized modal forms) so Admins, Doctors, and Patients all experience the exact same high-quality interface patterns.

---

## Phase 7: Frontend Integration (Role by Role)
- **Plan & Implement Loop**:
  1. **Public / Buyers**: Build the eCommerce pharmacy experience, shopping cart, online/cash payment flows, and the PDF upload/validation UX.
  2. **Doctors**: Build the dashboard for patient management, medical history, dynamic prescription issuing, and billing.
  3. **Admins**: Build the dashboard for user management and comprehensive inventory control.

---

## Phase 8: Final Polish & Deployment Preparation
- **Plan**: Conduct a full walkthrough of all workflows.
- **Implement**: Smooth out animations, enhance error states, ensure responsive design (mobile-friendly), and prepare the build scripts.

# USER TIDBITS: 
- It is preferable to download all minimized files for each external framework to minimize the number of break points (i.e. Angular servers down or Icons external servers down etc)
- First build functionality, then we will see some theme options for the final product to implement to the Tailwind CSS
- regenerate logo3.png ??? ← think about it 
