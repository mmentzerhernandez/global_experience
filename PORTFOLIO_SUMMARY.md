# WriteTrace Extension — Portfolio Summary

## Project Overview

**WriteTrace Extension** is a full-stack web application that enables users to process documents through a freemium model. Users get 100 free document analyses, with the option to upgrade to premium subscriptions for unlimited access. The application integrates Google OAuth authentication, Stripe payments, and a serverless architecture built on Firebase.

---

## 🎯 Key Features

### User Authentication
- **Google OAuth Sign-In** — Seamless authentication via Firebase Auth
- Secure session management with Firebase token handling
- User state persistence across sessions

### Freemium Model
- **Free Tier:** 100 document processing limit per user
- **Premium Tier:** Unlimited document processing via Stripe subscriptions
- Usage tracking and enforcement through Cloud Functions

### Payment Processing
- **Stripe Integration** — Complete checkout flow with Firebase Stripe Extension
- Subscription management and automatic renewal
- Real-time synchronization of payment status to user database

### Document Processing
- Access control enforced via HTTPS callable Cloud Functions
- Transaction-based consistency for document tracking
- Chrome extension integration for in-browser processing

### Analytics
- **Vercel Analytics** integration for performance monitoring
- Firebase Analytics for user behavior tracking

---

## 🏗️ Architecture Overview

### Frontend Layer
- **Framework:** Next.js 16 with App Router
- **UI Library:** React 19 with Radix UI components
- **Styling:** Tailwind CSS v4 for responsive design
- **Form Handling:** React Hook Form with Zod validation
- **Component Library:** Comprehensive Radix UI component set (modals, dropdowns, tables, etc.)

### Backend Layer
- **Database:** Cloud Firestore with security rules
- **Authentication:** Firebase Authentication with Google OAuth provider
- **Serverless Functions:** Cloud Functions (TypeScript)
  - `checkDocAccess()` — HTTPS callable function for document access validation
  - `syncStripeSubscription()` — Firestore trigger for subscription synchronization
- **Real-time Updates:** Firestore listeners for reactive UI updates

### Payment Integration
- **Stripe:** Direct API integration with Firebase Stripe Extension
- **Checkout Flow:** Client-side session creation with Stripe-hosted checkout
- **Webhook Integration:** Automatic status synchronization from Stripe events

### Data Model
```
users/{uid}
├── isPremium: boolean
└── usageCount: integer

processed_docs/{uid}_{docId}
├── uid: string
├── docId: string
└── timestamp: date

customers/{uid}/checkout_sessions/{id}
├── price: string
├── success_url: string
├── cancel_url: string
└── url: string (injected by extension)

customers/{uid}/subscriptions/{id}
├── status: string
└── [Stripe extension managed]
```

---

## 🛠️ Technical Skills Demonstrated

### Frontend Development
✓ **React & Next.js** — App Router, server/client components, API routes  
✓ **TypeScript** — Type-safe component development  
✓ **Styling** — Tailwind CSS, responsive design, dark mode support  
✓ **Component Design** — Reusable, accessible UI components  
✓ **Form Handling** — Validation, error handling, user feedback  
✓ **State Management** — React hooks, context for global state  

### Backend & Cloud Architecture
✓ **Firebase Services** — Auth, Firestore, Cloud Functions, Hosting  
✓ **Serverless Functions** — HTTPS callables, Firestore triggers, TypeScript  
✓ **Database Design** — Firestore schema design, security rules, transactions  
✓ **Real-time Database** — Listeners, snapshots, reactive updates  
✓ **Security Rules** — Document-level access control, authentication gates  

### Payment Integration
✓ **Stripe API** — Subscription management, checkout sessions  
✓ **Payment Flow Design** — Cart to checkout to confirmation  
✓ **Webhook Handling** — Event-driven subscription synchronization  
✓ **Firebase Stripe Extension** — Integration and configuration  

### Full-Stack Development
✓ **End-to-end Features** — Authentication → Checkout → Document Processing  
✓ **API Integration** — External service communication (Stripe, Google OAuth)  
✓ **Environment Management** — Configuration across dev/staging/production  
✓ **Deployment** — Firebase Hosting, Cloud Functions, Firestore rules  

### Development Practices
✓ **Version Control** — Git, pull requests, collaborative workflows  
✓ **Code Quality** — ESLint, TypeScript strict mode  
✓ **Documentation** — Architecture diagrams, setup guides  
✓ **Testing** — Firebase emulator compatibility  

---

## 📦 Technology Stack

### Frontend
- **Next.js 16** — React framework with server-side rendering
- **React 19** — UI library with hooks
- **TypeScript 5.7** — Type-safe JavaScript
- **Tailwind CSS 4** — Utility-first styling
- **Radix UI** — Unstyled, accessible component primitives
- **React Hook Form** — Lightweight form validation
- **Zod** — Schema validation library
- **date-fns** — Date manipulation utilities
- **Lucide React** — Icon library
- **Vercel Analytics** — Performance monitoring

### Backend
- **Firebase Admin SDK** — Backend authentication and database access
- **Cloud Firestore** — NoSQL database
- **Cloud Functions** — Serverless compute
- **Firebase Authentication** — Identity management
- **Firebase Hosting** — Web hosting and CDN

### Payments
- **Stripe API** — Payment processing
- **Firebase Stripe Extension** — Managed integration

### Development Tools
- **Node.js & npm** — JavaScript runtime and package management
- **PostCSS** — CSS transformation
- **ESLint** — Code quality linting

---

## 🚀 What Was Accomplished

### Core Application Features
1. **Fully functional authentication system** with Google OAuth sign-in
2. **Payment infrastructure** with Stripe subscription management
3. **Usage tracking and enforcement** with Cloud Functions
4. **Real-time database synchronization** between Stripe and Firestore
5. **Responsive, accessible UI** with modern component library
6. **Production-ready deployment** pipeline with Firebase

### Architecture Achievements
1. **Serverless, scalable design** — Cloud Functions handle all business logic
2. **Transactional consistency** — Document processing with Firestore transactions
3. **Security-first approach** — Firestore rules enforce access control
4. **Event-driven updates** — Subscription status syncs automatically via webhooks
5. **Real-time UI updates** — Firestore listeners for reactive features

### Developer Experience
1. **Clean, maintainable codebase** with TypeScript and modular components
2. **Comprehensive documentation** including architecture diagrams
3. **Easy local development** with Firebase emulator compatibility
4. **One-command deployment** to production with Firebase CLI

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| **Framework** | Next.js 16 + React 19 |
| **Languages** | TypeScript, JavaScript |
| **UI Components** | 27 Radix UI primitives |
| **Cloud Functions** | 2 (access control, subscription sync) |
| **Collections** | 4 main (users, processed_docs, customers, products) |
| **Payment Provider** | Stripe (via Firebase Extension) |
| **Hosting** | Firebase Hosting + Cloud Functions |

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

1. **Full-stack JavaScript development** from database to UI
2. **Modern React patterns** including server components and hooks
3. **Cloud architecture** with serverless functions and NoSQL databases
4. **Payment system integration** including PCI-compliant checkout flows
5. **Security implementation** with authentication, authorization, and data validation
6. **DevOps basics** including environment management and deployment automation
7. **Team collaboration** through clear documentation and version control

---

## 🔗 Live Demo & Deployment

- **Hosted on:** Firebase Hosting
- **Project ID:** `writetraceextension-db77b`
- **Database:** Cloud Firestore (NAM5 multi-region)

---

## 📝 Key Files

| File | Purpose |
|------|---------|
| `app/page.tsx` | Landing page with hero, features, testimonials |
| `app/login/page.tsx` | Google OAuth sign-in page |
| `app/upgrade/page.tsx` | Pricing & Stripe checkout page |
| `lib/firebase.ts` | Firebase SDK initialization |
| `functions/src/checkDocAccess.ts` | Document access validation |
| `functions/src/syncStripeSubscription.ts` | Subscription synchronization |
| `firestore.rules` | Security rules for Firestore |
| `ARCHITECTURE.md` | Detailed architecture documentation |

---

## ✨ Highlights

**What Makes This Special:**
- ✅ Complete freemium implementation with payment processing
- ✅ Real-time synchronization between multiple services
- ✅ Transactional consistency with Cloud Functions
- ✅ Production-grade security rules and access control
- ✅ Responsive, accessible UI with modern component library
- ✅ Comprehensive documentation and architecture diagrams

This is a **portfolio-ready, production-quality application** demonstrating full-stack development expertise across frontend, backend, cloud infrastructure, and payment systems.
