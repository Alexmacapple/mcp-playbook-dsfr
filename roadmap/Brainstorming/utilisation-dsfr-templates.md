# Utilisation du DSFR et création de templates dans Ecosystème

## 📦 Intégration du Design System Français (DSFR)

### Installation et configuration

Le projet utilise **@codegouvfr/react-dsfr v1.26.0**, la librairie React officielle du Design System de l'État français.

#### Configuration initiale (main.tsx)
```typescript
import '@codegouvfr/react-dsfr/dsfr/dsfr.css'
import '@codegouvfr/react-dsfr/dsfr/utility/icons/icons.css'
import { startReactDsfr } from '@codegouvfr/react-dsfr/spa';

// Initialisation avec détection automatique du thème système
startReactDsfr({ defaultColorScheme: 'system' });
```

### Composants DSFR natifs utilisés

Le projet importe et utilise **761 instances** de composants DSFR à travers 24 fichiers :

| Composant | Utilisation | Exemple |
|-----------|------------|---------|
| **Header** | Navigation principale | App.tsx - Menu avec 5 sections |
| **Footer** | Pied de page institutionnel | App.tsx - Liens légaux et accessibilité |
| **Button** | Actions et interactions | 200+ instances |
| **Card** | Cartes d'information | Dashboard, listes |
| **Alert** | Messages système | Erreurs, succès |
| **Badge** | Statuts et labels | Certificats, conformité |
| **Table** | Données tabulaires | Listes sites/domaines |
| **Input** | Champs de formulaire | Formulaires création/édition |
| **Select** | Listes déroulantes | Filtres et sélections |
| **Tabs** | Navigation par onglets | Détail site (7 onglets) |

## 🎨 Système de templates personnalisés

### Architecture des templates DSFR

Le fichier **`DSFRComponents.tsx`** centralise 7 templates réutilisables qui encapsulent les composants DSFR avec une logique métier :

#### 1. DSFRStatCard - Carte de statistique
```typescript
<DSFRStatCard
  title="Total Sites"
  value={stats.total}
  iconId="fr-icon-global-line"
  color="success"
  description="Sites actifs"
/>
```
**Utilisation** : Dashboard pour afficher les KPIs (sites actifs, certificats, conformité)

#### 2. DSFRLoadingSpinner - Indicateur de chargement
```typescript
<DSFRLoadingSpinner 
  message="Chargement des données..." 
  size="lg" 
/>
```
**Utilisation** : États de chargement asynchrone avec animation CSS personnalisée

#### 3. DSFREmptyState - État vide
```typescript
<DSFREmptyState
  title="Aucun site trouvé"
  description="Créez votre premier site"
  iconId="fr-icon-add-circle-line"
  actionButton={{
    label: "Créer un site",
    onClick: handleCreate
  }}
/>
```
**Utilisation** : Listes vides avec call-to-action

#### 4. DSFRStatusBadge - Badge de statut
```typescript
<DSFRStatusBadge 
  status="valid" 
  label="Certificat valide" 
  small={false}
/>
```
**Utilisation** : Indicateurs visuels de statut (valide, warning, error, info)

#### 5. DSFRSectionHeader - En-tête de section
```typescript
<DSFRSectionHeader
  title="Gestion des sites"
  subtitle="53 sites actifs"
  actionButton={{
    label: "Nouveau site",
    onClick: handleNewSite,
    iconId: "fr-icon-add-line"
  }}
/>
```
**Utilisation** : En-têtes de pages avec actions contextuelles

#### 6. DSFRSearchBar - Barre de recherche
```typescript
<DSFRSearchBar
  placeholder="Rechercher un site..."
  value={searchTerm}
  onChange={setSearchTerm}
  onSearch={handleSearch}
/>
```
**Utilisation** : Recherche dans les listes et tableaux

#### 7. DSFRSimplePagination - Pagination
```typescript
<DSFRSimplePagination
  currentPage={currentPage}
  totalPages={totalPages}
  onPageChange={setCurrentPage}
/>
```
**Utilisation** : Navigation dans les résultats paginés

## 🎯 Utilisation des couleurs et tokens DSFR

### Système de couleurs sémantiques
```typescript
// Utilisation du système de couleurs DSFR via l'objet fr
fr.colors.decisions.background.actionHigh.blueFrance.default  // Bleu France
fr.colors.decisions.background.flat.success.default          // Vert succès
fr.colors.decisions.background.flat.error.default            // Rouge erreur
fr.colors.decisions.background.flat.warning.default          // Orange warning
```

### Classes utilitaires DSFR
```typescript
// Espacement
fr.cx('fr-mt-4w')     // margin-top: 4 unités
fr.cx('fr-px-2w')     // padding horizontal: 2 unités

// Typographie
fr.cx('fr-h1')        // Titre niveau 1
fr.cx('fr-text--lg')  // Texte large
fr.cx('fr-text--bold') // Texte gras

// Layout
fr.cx('fr-container')  // Container responsive
fr.cx('fr-grid-row')   // Grille flexible
fr.cx('fr-col-12')     // Colonnes 12/12
```

## 📊 Statistiques d'utilisation

### Répartition par composant
- **27 fichiers** utilisent les composants DSFR
- **761 instances** totales de composants
- **100% des pages** respectent le DSFR
- **7 templates** personnalisés créés

### Pages principales et leur utilisation DSFR

| Page | Composants DSFR | Templates custom |
|------|-----------------|------------------|
| Dashboard | Card, Badge, Alert | StatCard, LoadingSpinner |
| SiteList | Table, Button, Input | SearchBar, Pagination, EmptyState |
| SiteDetail | Tabs, Card, Badge | SectionHeader, StatusBadge |
| CertificatesPage | Table, Badge, Alert | StatusBadge, LoadingSpinner |
| SiteForm | Input, Select, Button | SectionHeader |

## 🚀 Bonnes pratiques appliquées

### 1. Centralisation des templates
- Tous les templates dans `DSFRComponents.tsx`
- Export nommé pour chaque composant
- TypeScript pour la type-safety

### 2. Composition plutôt qu'héritage
- Templates qui wrappent les composants DSFR
- Props typées avec interfaces
- Valeurs par défaut sensées

### 3. Accessibilité garantie
- Attributs ARIA (`aria-hidden`, `aria-label`)
- Rôles sémantiques (`role="search"`)
- Classes screen-reader (`sr-only`)

### 4. Responsive par défaut
- Grille DSFR responsive
- Classes conditionnelles (`fr-col-12`, `fr-col-md-6`)
- Breakpoints DSFR respectés

### 5. Performance optimisée
- Composants fonctionnels React
- Pas de re-renders inutiles
- CSS-in-JS évité au profit des classes DSFR

## 🔄 Évolutions possibles

### Templates additionnels suggérés
1. **DSFRDataTable** : Table avec tri, filtre et export
2. **DSFRForm** : Formulaire avec validation DSFR
3. **DSFRNotification** : Système de notifications toast
4. **DSFRBreadcrumb** : Fil d'Ariane dynamique
5. **DSFRStepper** : Indicateur d'étapes

### Améliorations techniques
- Storybook pour documenter les templates
- Tests unitaires sur chaque template
- Dark mode avec les tokens DSFR
- Animations conformes aux guidelines

## 📚 Ressources

- [Documentation DSFR](https://www.systeme-de-design.gouv.fr/)
- [react-dsfr GitHub](https://github.com/codegouvfr/react-dsfr)
- [Composants DSFR](https://components.react-dsfr.codegouv.studio/)
- [Tokens de design](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/couleurs)

---

*Document généré le 11 septembre 2025*  
*Projet Ecosystème - Conformité DSFR v1.26.0*