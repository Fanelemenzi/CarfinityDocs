# Maintenance Form User Flow Guide

## Visual Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    START: MAINTENANCE FORM                  │
│                                                              │
│          ┌──────────────────────────────────────┐           │
│          │   Header: "Log Maintenance Work"    │           │
│          │   Gradient Blue Background           │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │      Progress Indicator: 1→2→3→4    │           │
│          │   (Step 1 highlighted, rest gray)    │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │      STEP 1: VEHICLE SELECTION      │           │
│          │           🚗 Section                 │           │
│          ├──────────────────────────────────────┤           │
│          │  Vehicle Dropdown                   │           │
│          │  [Select vehicle...]                │           │
│          │                                      │           │
│          │  ℹ️  Tip: Pick correct vehicle      │           │
│          ├──────────────────────────────────────┤           │
│          │  [← Previous] [Next →]              │           │
│          │        (Previous hidden)             │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │    STEP 2: WORK DETAILS              │           │
│          │        🔧 Section                    │           │
│          ├──────────────────────────────────────┤           │
│          │  Scheduled Maintenance               │           │
│          │  [-- Select maintenance task --]    │           │
│          │                                      │           │
│          │  Work Performed *                    │           │
│          │  ┌──────────────────────────────┐   │           │
│          │  │ [Detailed description...]   │   │           │
│          │  │ [Example provided]          │   │           │
│          │  └──────────────────────────────┘   │           │
│          │                                      │           │
│          │  Odometer Reading *                  │           │
│          │  [123456]                           │           │
│          │                                      │           │
│          │  Additional Notes                    │           │
│          │  [Optional observations...]         │           │
│          ├──────────────────────────────────────┤           │
│          │  [← Previous] [Next →]              │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │  STEP 3: DOCUMENTATION               │           │
│          │       📸 Section (Optional)          │           │
│          ├──────────────────────────────────────┤           │
│          │  ℹ️  Why document your work box    │           │
│          │                                      │           │
│          │  Service Photo:                      │           │
│          │  ╔════════════════════════════════╗  │           │
│          │  ║ 📷 Drop here or click browse  ║  │           │
│          │  ║ JPEG, PNG, GIF, WebP • Max 10MB  ║           │
│          │  ╚════════════════════════════════╝  │           │
│          │  [Image preview appears here]       │           │
│          │                                      │           │
│          │  Photo Category:                     │           │
│          │  [-- Select category --]            │           │
│          │                                      │           │
│          │  Photo Description:                  │           │
│          │  [Brief description...]             │           │
│          ├──────────────────────────────────────┤           │
│          │  [← Previous] [Next →]              │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │    STEP 4: REVIEW & SAVE             │           │
│          │        ✅ Section                    │           │
│          ├──────────────────────────────────────┤           │
│          │  ✅ "Ready to Save" success alert   │           │
│          │                                      │           │
│          │  ℹ️  What happens next...           │           │
│          │  • Record added to vehicle history   │           │
│          │  • Used for scheduling               │           │
│          │  • Supports warranty claims          │           │
│          ├──────────────────────────────────────┤           │
│          │  [← Previous] [SAVE RECORD]         │           │
│          │        (Both buttons visible)        │           │
│          └──────────────────────────────────────┘           │
│                            ↓                                 │
│          ┌──────────────────────────────────────┐           │
│          │   END: Form Submitted Successfully   │           │
│          │   (Redirect to maintenance history)  │           │
│          └──────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
```


## Screen-by-Screen Breakdown

### HEADER (All Steps)
```
┌─────────────────────────────────────────┐
│  [BLUE GRADIENT BACKGROUND]             │
│                                          │
│    Log Maintenance Work                  │
│    Keep your vehicle service history     │
│    organized and accurate                │
│                                          │
└─────────────────────────────────────────┘
```

**Design Elements:**
- Gradient blue background (visual anchor)
- Large, clear title (2rem, bold)
- Descriptive subtitle (smaller, lighter)
- Sets professional tone


### PROGRESS INDICATOR (All Steps)
```
Step 1          Step 2          Step 3          Step 4
  1               2               3               4
[BLUE]          [GRAY]          [GRAY]          [GRAY]
Vehicle ―― Work Details ―― Documentation ―― Review & Save
 Active          Future          Future          Future

Legend:
● Active   = Blue circle with glow
● Future   = Gray circle
● Completed = Green circle with checkmark
═══ Line   = Shows progression
```

**Responsive Behavior:**
- Desktop: All 4 steps visible in one line
- Tablet: Wraps to 2 rows if needed
- Mobile: Stacks vertically, lines hidden


### STEP 1: VEHICLE SELECTION

```
┌────────────────────────────────────────────────┐
│ 🚗 Select Your Vehicle                         │
├────────────────────────────────────────────────┤
│                                                 │
│ Vehicle *                                       │
│ (Choose the vehicle you're logging for)        │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ ▼ Select vehicle...                     │  │
│ └──────────────────────────────────────────┘  │
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ ℹ️  Tip: Pick the correct vehicle      │   │
│ │    Ensures accurate maintenance records  │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
├────────────────────────────────────────────────┤
│              [← Prev]    [Next →]              │
│                                                 │
│              (Previous button hidden)           │
└────────────────────────────────────────────────┘
```

**UX Notes:**
- Single field (not overwhelming)
- Icon helps identify section quickly
- Helpful tip explains importance
- Only "Next" button visible (no going back)


### STEP 2: WORK DETAILS

```
┌────────────────────────────────────────────────┐
│ 🔧 Work Details                                │
├────────────────────────────────────────────────┤
│                                                 │
│ Scheduled Maintenance Task                     │
│ (Select which task - optional)                 │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ ▼ -- Choose maintenance task --         │  │
│ │   • Oil Change - Due: 2026-07-15         │  │
│ │   • Tire Rotation - Due: 2026-08-20      │  │
│ └──────────────────────────────────────────┘  │
│                                                 │
│ Work Performed * ← REQUIRED                    │
│ (Be specific and detailed)                     │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ Replaced front brake pads (OEM spec),   │  │
│ │ inspected rotors (good condition),       │  │
│ │ bled brake system, test drive OK         │  │
│ └──────────────────────────────────────────┘  │
│ 📝 Example: "Replaced brake pads..."      │
│                                                 │
│ Odometer Reading * ← REQUIRED                  │
│ (Current mileage at time of service)           │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ 123456                                   │  │
│ └──────────────────────────────────────────┘  │
│ 📝 Record exact odometer - for warranty       │
│                                                 │
│ Additional Notes                               │
│ (Optional observations)                        │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │                                          │  │
│ └──────────────────────────────────────────┘  │
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ 💡 Pro Tip: Be Specific                 │   │
│ │    Details now = valuable record later   │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
├────────────────────────────────────────────────┤
│              [← Prev]    [Next →]              │
│           (Both buttons visible)                │
└────────────────────────────────────────────────┘
```

**Validation Triggers:**
- If user clicks "Next" without Work Performed:
  - Field borders turn red
  - Error message appears: "Work performed is required"
  - Error message animated in smoothly
  - User scrolls to field automatically

**Smart Features:**
- Scheduled maintenance auto-filtered by vehicle from Step 1
- If no vehicle selected in Step 1, shows placeholder: "Select a vehicle first"


### STEP 3: DOCUMENTATION

```
┌────────────────────────────────────────────────┐
│ 📸 Add Photos (Optional)                       │
├────────────────────────────────────────────────┤
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ ℹ️  📋 Why Document Your Work?          │   │
│ │                                          │   │
│ │ Photos create proof of work, help future│   │
│ │ technicians, and provide before/after   │   │
│ │ evidence for warranty claims             │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
│ Service Photo                                   │
│                                                 │
│ ╔════════════════════════════════════════╗    │
│ ║         📷 Drop your photo here        ║    │
│ ║           or click to browse           ║    │
│ ║                                        ║    │
│ ║ JPEG, PNG, GIF, WebP • Max 10MB        ║    │
│ ╚════════════════════════════════════════╝    │
│                                                 │
│ [After file selected:]                         │
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │                                          │   │
│ │  ┌──────────────────┐                  │   │
│ │  │                  │   ×  ← Remove btn│   │
│ │  │  [Image Preview] │                  │   │
│ │  │                  │                  │   │
│ │  └──────────────────┘                  │   │
│ │                                          │   │
│ │  File: IMG_1234.jpg                     │   │
│ │  Size: 2.3 MB                           │   │
│ │                                          │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
│ Photo Category                                  │
│ (What does this photo show?)                   │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ ▼ -- Select category --                 │  │
│ │   • Before Service                       │  │
│ │   • During Service                       │  │
│ │   • After Service                        │  │
│ │   • Parts/Components                     │  │
│ │   • Damage/Issue Found                   │  │
│ └──────────────────────────────────────────┘  │
│                                                 │
│ Photo Description                              │
│ (Briefly describe what's shown)                │
│                                                 │
│ ┌──────────────────────────────────────────┐  │
│ │ New brake pads installed - front left    │  │
│ └──────────────────────────────────────────┘  │
│ 📝 Example: "Replaced brake pads..."         │
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ ℹ️  Photo Tips                          │   │
│ │ • Clear, well-lit photos               │   │
│ │ • Show before/after conditions         │   │
│ │ • Include part numbers when visible    │   │
│ │ • Document any damage found            │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
├────────────────────────────────────────────────┤
│              [← Prev]    [Next →]              │
│           (Both buttons visible)                │
└────────────────────────────────────────────────┘
```

**Drag-and-Drop Behavior:**
```
Before drag:         During hover:         After drop:
┌──────────────┐    ┌──────────────┐     ┌──────────────┐
│ 📷 Drop here │    │ 📷 Drop here │     │ ✅ File ready│
│ border: gray │    │ border: blue │     │ border: green│
│              │    │ glow: blue   │     │              │
└──────────────┘    └──────────────┘     └──────────────┘
```

**File Upload Validation:**
```
Valid file selected:
✅ "IMG_1234.jpg" (2.3 MB) → Preview shows thumbnail

Invalid file selected:
❌ File too large (15 MB) → Error: "Image too large. Max 10MB"
❌ Wrong format (.pdf)   → Error: "Invalid image format"
❌ Corrupted image       → Error: "Could not read file"
```


### STEP 4: REVIEW & SAVE

```
┌────────────────────────────────────────────────┐
│ ✅ Review & Save                               │
├────────────────────────────────────────────────┤
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ ✅ Ready to Save                        │   │
│ │                                          │   │
│ │ All required fields are complete.       │   │
│ │ Click save to finalize the maintenance  │   │
│ │ record.                                  │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
│ ┌─────────────────────────────────────────┐   │
│ │ ℹ️  Once You Save...                    │   │
│ │                                          │   │
│ │ Your maintenance record will be:        │   │
│ │ • Added to the vehicle's service       │   │
│ │   history                               │   │
│ │ • Used to calculate future maintenance │   │
│ │   schedules                             │   │
│ │ • Available for warranty claims         │   │
│ └─────────────────────────────────────────┘   │
│                                                 │
├────────────────────────────────────────────────┤
│              [← Prev]    [SAVE RECORD]         │
│           (Both buttons visible)                │
└────────────────────────────────────────────────┘

[During submission:]

┌────────────────────────────────────────────────┐
│                                                 │
│              🔄 Saving...                       │
│          Please wait...                        │
│                                                 │
│       [Loading animation]                      │
│                                                 │
└────────────────────────────────────────────────┘

[After submission:]

Redirect to: /maintenance/success/ or /vehicle/{id}/
```

**Save Button States:**
```
Normal:        Hover:         Disabled:
[SAVE RECORD]  [SAVE RECORD]  [SAVING...]
blue gradient  lighter shade  grayed out
subtle shadow  elevated       no pointer
```


## Mobile Responsive Views

### Mobile (375px - iPhone SE)

```
┌────────────────────────┐
│ Log Maintenance Work   │
│ Keep organized         │
└────────────────────────┘

Progress: [1] 2 3 4
(Stacked vertically)

┌────────────────────────┐
│ 🚗 Select Vehicle      │
├────────────────────────┤
│ Vehicle *              │
│ ┌──────────────────┐   │
│ │ Select vehicle..│   │
│ └──────────────────┘   │
│                        │
│ Helpful tip            │
├────────────────────────┤
│  [Next →]              │
│  (Full width)          │
└────────────────────────┘
```

**Mobile Optimizations:**
- Single column layout
- Full-width buttons
- Larger touch targets (44px+)
- Simplified progress indicator
- Readable font sizes
- Compact spacing


### Tablet (768px - iPad)

```
┌─────────────────────────────────────┐
│ Log Maintenance Work                │
└─────────────────────────────────────┘

1─Vehicle  2─Work Details  3─Docs  4─Save
(Still shows all 4 steps)

┌─────────────────────────────────────┐
│ 🚗 Select Your Vehicle              │
├─────────────────────────────────────┤
│ Vehicle *                           │
│ ┌─────────────────────────────────┐ │
│ │ Select vehicle...              │ │
│ └─────────────────────────────────┘ │
│                                     │
│ ℹ️  Helpful tip text               │
├─────────────────────────────────────┤
│ [← Prev]         [Next →]           │
│    (Side by side, more space)       │
└─────────────────────────────────────┘
```


## Error State Examples

### Missing Required Field (Work Performed)

```
┌────────────────────────────────────────┐
│ 🔧 Work Details                        │
├────────────────────────────────────────┤
│                                        │
│ [User clicks Next without filling in] │
│                                        │
│ ┌────────────────────────────────────┐ │
│ │ ❌ Please fix these errors:        │ │
│ │    • Work performed is required     │ │
│ │    • Odometer reading is required  │ │
│ └────────────────────────────────────┘ │
│                                        │
│ Work Performed * ← REQUIRED            │
│ ┌────────────────────────────────────┐ │
│ │  ← Red border, error background    │ │
│ └────────────────────────────────────┘ │
│ ❌ Work performed is required         │
│                                        │
│ Odometer Reading * ← REQUIRED          │
│ ┌────────────────────────────────────┐ │
│ │  ← Red border, error background    │ │
│ └────────────────────────────────────┘ │
│ ❌ Odometer reading is required       │
│                                        │
├────────────────────────────────────────┤
│ [← Prev]    [Next →]                  │
└────────────────────────────────────────┘
```


### Invalid File Upload

```
Service Photo

[User selects 15MB .pdf file]

╔════════════════════════════════╗
║ ❌ Image file size cannot      ║
║    exceed 10MB. Current:       ║
║    14.8 MB                     ║
╚════════════════════════════════╝
```


## Keyboard Navigation

**Tab Order:**
1. Vehicle dropdown
2. Next button
3. [On Step 2] Scheduled Maintenance dropdown
4. Work Performed textarea
5. Odometer Reading input
6. Notes textarea
7. Previous button
8. Next button
9. [On Step 3] File input
10. Image Type dropdown
11. Image Description textarea
12. Previous button
13. Next button
14. [On Step 4] Previous button
15. Save Record button

**Keyboard Shortcuts:**
- Tab: Move to next field
- Shift+Tab: Move to previous field
- Enter: Submit form (on final step)
- Space: Toggle dropdown on focused select
- Escape: Close dropdown (if supported)


## Accessibility Features

### Screen Reader Announcements

```
"Log Maintenance Work dialog, region"
"Step 1 of 4, Vehicle Selection"
"Vehicle dropdown, required field, choose the vehicle you're logging for"
"Next button"
"Error, work performed is required"
"[Forms will announce validation errors automatically]"
```

### Focus Indicators

```
Focused field:
┌──────────────────────┐
│ [Input field]     ← Blue outline (3px)
└──────────────────────┘
  Blue glow/shadow
  Light blue background

Focused button:
[NEXT →] ← Focus ring visible
 High contrast border
```


## Animations & Transitions

### Section Change Animation
```css
Duration: 400ms
Direction: Fade in from bottom
Effect: Smooth, professional
```

### Error Message Animation
```css
Duration: 300ms
Direction: Slide down from top
Effect: Grabs attention without jarring
```

### Image Preview Animation
```css
Duration: 300ms
Effect: Scale up (0.95 → 1) while fading in
Result: Smooth appearance
```


## Loading & Submission States

### Before Click
```
[SAVE RECORD] ← Blue gradient, ready
```

### During Submission
```
[⏳ SAVING...] ← Spinner animating, disabled
Form grayed out, no interaction
```

### After Success
```
Redirect to: Vehicle maintenance history
Page shows: "Maintenance record saved successfully"
Toast notification (optional): "✅ Saved!"
```

### Error During Submission
```
Alert appears: "Error saving record. Please try again."
Form re-enables for editing
User can correct and resubmit
```


## Summary

This redesign transforms the maintenance logging experience from a daunting, overwhelming single-page form into an intuitive, guided 4-step wizard that feels modern and professional while maintaining all required functionality.

The progressive disclosure approach dramatically improves user success rate while the modern design encourages users to provide detailed, accurate maintenance records.

