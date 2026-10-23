const TOURS = {
  yunanistan: {
    id: 'yunanistan',
    file: 'yunanistan-turu-23-29-ekim-2026-v5.json',
    mark: 'GR',
    brand: 'Yunanistan Rotası',
    heroImg: 'assets/greece-hero.jpg',
    heroAlt: 'Meteora manastırları ve antik dağ yolu manzarası',
    eyebrow: '23 — 29 Ekim 2026',
    heroTitle: 'Ege ve Antik Makedonya.<br><em>Tek unutulmaz rota.</em>',
    heroLead: 'İstanbul’dan Meteora kayalıklarına, Selanik ve Kavala’dan Ege kıyılarına uzanan 1.895 kilometrelik güvenli otoyol yolculuğu.',
    routeKicker: 'Genel bakış',
    routeHeading: 'Altı günde<br><em>Kuzey Yunanistan</em>',
    hasSosCard: true
  }
};

let currentTourKey = 'yunanistan';
let trip;

const $ = (selector) => document.querySelector(selector);
const formatDate = (date) => {
  if (!date) return '';
  const str = String(date).trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(str)) {
    const d = new Date(`${str}T12:00:00`);
    if (!isNaN(d.getTime())) {
      return new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long' }).format(d);
    }
  }
  return str.replace(/(\d{4})-(\d{2})-(\d{2})/g, (match, y, m, d) => {
    const dateObj = new Date(Number(y), Number(m) - 1, Number(d), 12, 0, 0);
    return new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long' }).format(dateObj);
  });
};
const mapsSearch = (place) => `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(place)}`;
const externalLink = (url, label = 'Kaynağı aç') => url ? `<a class="inline-link" href="${url}" target="_blank" rel="noreferrer">${label} ↗</a>` : '';
const list = (items, className = 'plain-list') => items?.length ? `<ul class="${className}">${items.map(item => `<li>${item}</li>`).join('')}</ul>` : '';
const yesNo = (value) => value === null || value === undefined ? 'Henüz belirlenmedi' : value ? 'Evet' : 'Hayır';
const statusLabel = (status) => ({
  Verified: 'Doğrulandı',
  VerifiedByTravelSource: 'Seyahat kaynağıyla doğrulandı',
  Provisional: 'Geçici seçim',
  Flexible: 'Esnek',
  VerifyBeforeTravel: 'Seyahatten önce doğrula'
}[status] || status);

const distance = (value) => {
  if (!value) return '—';
  if (typeof value === 'number') return `${value} km`;
  if (value.exact) return `${value.exact} km`;
  return `${value.min}–${value.max} km`;
};

const driveTime = (day) => {
  const value = day.estimatedDrivingHoursIncludingNormalBorders || day.estimatedDrivingHoursIncludingNormalBorder || day.estimatedDrivingHoursWithoutStops || day.estimatedDrivingHours;
  if (!value) return `${day.estimatedDrivingMinutes?.min || 0}–${day.estimatedDrivingMinutes?.max || 0} dk`;
  return typeof value === 'number' ? `${value} saat` : `${value.min}–${value.max} saat`;
};

function renderSummary() {
  const tourCfg = TOURS[currentTourKey];
  const summary = trip.tripSummary;
  
  // Hero Images & Texts
  $('#heroImg').src = tourCfg.heroImg;
  $('#heroImg').alt = tourCfg.heroAlt;
  $('#brandMark').textContent = tourCfg.mark;
  $('#brandName').textContent = tourCfg.brand;
  $('#footerMark').textContent = tourCfg.mark;
  $('#footerBrandName').textContent = tourCfg.brand;
  $('#heroDates').textContent = tourCfg.eyebrow;
  $('#heroTitle').innerHTML = tourCfg.heroTitle;
  $('#heroLead').textContent = tourCfg.heroLead;
  $('#routeKicker').textContent = tourCfg.routeKicker;
  $('#routeHeading').innerHTML = tourCfg.routeHeading;

  // Toggle SOS buttons depending on tour
  const sosDisplay = tourCfg.hasSosCard ? 'inline-flex' : 'none';
  if ($('#openSosBtn')) $('#openSosBtn').style.display = sosDisplay;
  if ($('#heroSosBtn')) $('#heroSosBtn').style.display = sosDisplay;
  if ($('#guideSosTab')) $('#guideSosTab').style.display = sosDisplay;

  const totalDist = summary.estimatedTotalDistanceKm.exact || summary.estimatedTotalDistanceKm.min;
  const stats = [
    [`${summary.durationDays} gün`, 'Süre'],
    [`${totalDist} km`, 'Toplam rota'],
    [`${summary.countries.length} ülke`, 'Keşfedilecek'],
    [`${summary.durationNights} gece`, 'Konaklama']
  ];
  $('#heroStats').innerHTML = stats.map(([value, label]) => `<div class="stat"><strong>${value}</strong><small>${label}</small></div>`).join('');
  
  $('#routeIntro').textContent = `${summary.countries.join(', ')} boyunca uzanan yaklaşık ${totalDist} kilometrelik rota; tarih, kültür ve manzarayı konforlu bir sürüşle buluşturuyor.`;
  const dateLabel = `${formatDate(summary.startDate)} — ${formatDate(summary.endDate)} ${new Date(`${summary.endDate}T12:00:00`).getFullYear()}`;
  $('#heroDates').textContent = dateLabel;
  $('#footerDates').textContent = dateLabel;
  document.title = `${trip.metadata.title} · ${dateLabel}`;
  
  ['headerMap', 'heroMap', 'routeMap'].forEach(id => {
    const el = $(`#${id}`);
    if (el) el.href = trip.approvedRoute.googleMapsUrl;
  });
  $('#disclaimer').textContent = `${trip.metadata.distanceAndTimeDisclaimer} ${trip.metadata.bookingStatus}`;
}

function renderRoute() {
  const stops = trip.approvedRoute.orderedStops;
  $('#routeLine').style.gridTemplateColumns = `repeat(${stops.length}, minmax(130px, 1fr))`;
  $('#routeLine').style.minWidth = `${stops.length * 130}px`;
  $('#routeLine').innerHTML = stops.map((city, index) => `
    <a class="route-stop" href="${mapsSearch(city)}" target="_blank" rel="noreferrer" aria-label="${city} konumunu Google Maps'te aç">
      <strong>${city}</strong>
      <small>${index + 1}. durak</small>
    </a>`).join('');

  let decisionsHtml = '';
  if (trip.routeDecisions.safetyStrategy && trip.routeDecisions.thessalonikiStrategy) {
    // Yunanistan Rota Kararları
    const safety = trip.routeDecisions.safetyStrategy;
    const thess = trip.routeDecisions.thessalonikiStrategy;
    const nightRest = trip.routeDecisions.nightRestAreaStrategy;
    const excludedPlaces = trip.routeDecisions.placesIntentionallyNotIncluded.map(item => `
      <article class="decision-card compact">
        <span class="decision-icon" aria-hidden="true">−</span>
        <div><small>Rota Tercihi</small><h3>${item.place}</h3><p>${item.reason}</p></div>
      </article>`).join('');

    decisionsHtml = `
      <summary>
        <div class="decision-summary-copy">
          <p class="kicker">Güvenli sürüş ve rota kararları</p>
          <h3>Neden bu güzergah?</h3>
          <p>İlk yurt dışı sürüşüne özel otoyol tercihleri, gece uyku molası stratejisi, metro Park & Ride sistemi ve elenen dağ yolları gerekçeleri.</p>
        </div>
        <span class="decision-toggle" aria-hidden="true">+</span>
      </summary>
      <div class="decisions-content">
        <div class="decision-feature">
          <span class="decision-icon keep" aria-hidden="true">✓</span>
          <div>
            <small>Ana Prensip · ${safety.status}</small>
            <h3>${safety.title}</h3>
            <p>${safety.explanation}</p>
            <div style="margin-top:12px; padding-top:10px; border-top:1px solid rgba(255,255,255,.15)">
              <small style="color:#ffc5a3">${thess.title}</small>
              <p style="margin-top:4px;">${thess.explanation}</p>
            </div>
            ${nightRest ? `
            <div style="margin-top:12px; padding-top:10px; border-top:1px solid rgba(255,255,255,.15)">
              <small style="color:#ffd1b8">🌙 ${nightRest.title}</small>
              <p style="margin-top:4px;">${nightRest.explanation}</p>
            </div>` : ''}
          </div>
        </div>
        <div class="decision-grid">${excludedPlaces}</div>
      </div>`;
  } else if (trip.routeDecisions.kosovoDecision) {
    // Balkan Rota Kararları
    const kosovo = trip.routeDecisions.kosovoDecision;
    const excludedCountries = (trip.tripSummary.excludedCountries || []).map(item => `
      <article class="decision-card">
        <span class="decision-icon" aria-hidden="true">×</span>
        <div><small>Rota dışında</small><h3>${item.country}</h3><p>${item.reason}</p></div>
      </article>`).join('');
    const excludedPlaces = (trip.routeDecisions.placesIntentionallyNotIncluded || []).map(item => `
      <article class="decision-card compact">
        <span class="decision-icon" aria-hidden="true">−</span>
        <div><small>Başka bir geziye</small><h3>${item.place}</h3><p>${item.reason}</p></div>
      </article>`).join('');

    decisionsHtml = `
      <summary>
        <div class="decision-summary-copy">
          <p class="kicker">Rota kararları</p>
          <h3>Neden bu rota?</h3>
          <p>Rotaya alınan ve sonraki gezilere bırakılan durakların gerekçelerini görüntüle.</p>
        </div>
        <span class="decision-toggle" aria-hidden="true">+</span>
      </summary>
      <div class="decisions-content">
        <div class="decision-feature">
          <span class="decision-icon keep" aria-hidden="true">✓</span>
          <div>
            <small>Rotada tutuldu · ${kosovo.status}</small>
            <h3>Kosova · Yalnızca Prizren</h3>
            <p>${kosovo.explanation}</p>
            <p class="decision-excluded"><strong>Bu turda yok:</strong> ${kosovo.notIncluded.join(', ')}</p>
          </div>
        </div>
        <div class="decision-grid">${excludedCountries}${excludedPlaces}</div>
      </div>`;
  }
  $('#routeDecisions').innerHTML = decisionsHtml;
}

function renderDayTabs() {
  $('#dayTabs').innerHTML = trip.dailyItinerary.map((day, index) => `
    <button class="day-tab ${index === 0 ? 'active' : ''}" role="tab" aria-selected="${index === 0}" data-day="${index}">
      <strong>${day.day}. Gün</strong><span>${formatDate(day.date)}</span>
    </button>`).join('');

  $('#dayTabs').onclick = (event) => {
    const button = event.target.closest('[data-day]');
    if (!button) return;
    document.querySelectorAll('.day-tab').forEach(tab => {
      tab.classList.remove('active');
      tab.setAttribute('aria-selected', 'false');
    });
    button.classList.add('active');
    button.setAttribute('aria-selected', 'true');
    renderDay(Number(button.dataset.day));
  };
  renderDay(0);
}

function renderMealOption(option, isAlternative = false) {
  if (!option) return '';
  const title = option.venueName || option.type || 'Esnek mekân seçimi';
  return `<div class="meal-option ${isAlternative ? 'alternative' : 'primary'}">
    <div class="meal-option-head">
      <strong>${title}</strong>
      ${option.verificationStatus ? `<span class="status-badge status-${option.verificationStatus.toLowerCase()}">${statusLabel(option.verificationStatus)}</span>` : ''}
    </div>
    ${option.type && option.venueName ? `<p><b>Tür:</b> ${option.type}</p>` : ''}
    ${option.reason ? `<p>${option.reason}</p>` : ''}
    ${option.recommendedFoods?.length ? `<p><b>Önerilenler:</b> ${Array.isArray(option.recommendedFoods) ? option.recommendedFoods.join(', ') : option.recommendedFoods}</p>` : ''}
    ${option.estimatedCostForTwo ? `<p><b>Tahmini tutar:</b> ${option.estimatedCostForTwo}</p>` : ''}
    ${option.reservationRequired !== undefined ? `<p><b>Rezervasyon:</b> ${yesNo(option.reservationRequired)}</p>` : ''}
    ${option.phone ? `<p><b>Telefon:</b> <a href="tel:${option.phone.replace(/\s/g, '')}">${option.phone}</a></p>` : ''}
    ${option.mapUrl ? `<p><a class="inline-link" href="${option.mapUrl}" target="_blank" rel="noreferrer">Google Maps'te Aç ↗</a></p>` : ''}
  </div>`;
}

function renderMeal(meal) {
  const urls = [...(meal.sourceUrls || []), ...(meal.sourceUrl ? [meal.sourceUrl] : [])];
  return `<details class="meal-card">
    <summary>
      <div>
        <small>${meal.timeRange} · ${meal.location}</small>
        <strong>${meal.mealType}</strong>
      </div>
      <span>${meal.primaryOption?.venueName || meal.primaryOption?.type || 'Esnek plan'} ＋</span>
    </summary>
    <div class="meal-body">
      ${meal.strategy ? `<p class="meal-strategy"><b>Strateji:</b> ${meal.strategy}</p>` : ''}
      ${meal.recommendedFoods?.length ? `<div class="food-tags">${meal.recommendedFoods.map(food => `<span>${food}</span>`).join('')}</div>` : ''}
      ${renderMealOption(meal.primaryOption)}
      ${meal.alternativeOptions?.length ? `<div class="meal-alternatives"><h5>Alternatifler</h5>${meal.alternativeOptions.map(option => renderMealOption(option, true)).join('')}</div>` : ''}
      ${meal.dietaryWarnings?.length ? `<div class="warning-box"><b>Yeme–içme uyarıları</b>${list(meal.dietaryWarnings)}</div>` : ''}
      ${urls.length ? `<div class="source-links">${urls.map((url, i) => externalLink(url, `Konum / Kaynak ${i + 1}`)).join('')}</div>` : ''}
    </div>
  </details>`;
}

function renderDailyPayments(notes) {
  return `<div class="payment-panel">
    <div class="currency-chips">${notes.currenciesNeeded.map(code => `<span>${code}</span>`).join('')}</div>
    <p><b>Nakit öneriliyor:</b> ${yesNo(notes.cashRecommended)}</p>
    ${notes.estimatedMealCostForTwo ? `<p><b>İki kişilik yemek tahmini:</b> ${notes.estimatedMealCostForTwo}</p>` : ''}
    <div class="payment-columns">
      <div><h5>Beklenen ödemeler</h5>${list(notes.expectedPayments)}</div>
      <div><h5>Dikkat</h5>${list(notes.warnings, 'warning-list')}</div>
    </div>
  </div>`;
}

function renderDay(index) {
  const day = trip.dailyItinerary[index];
  const overnight = day.overnight || '—';

  // Critical Alert Box (e.g. Vergina opening at 12:00, Mehmet Ali Paşa closing at 14:30)
  const alertHtml = day.criticalAlert ? `
    <div class="day-critical-alert">
      <span>⏰</span>
      <div><strong>Önemli Saat & Güzergah Uyarısı:</strong> ${day.criticalAlert}</div>
    </div>` : '';

  // Hotel Badge with Reservation Code
  const hotelHtml = day.hotel ? `
    <div class="day-hotel-badge">
      <span>🏨</span>
      <b>${day.hotel.name}</b>
      ${day.hotel.reservationCode ? `<span>Rez: <code>${day.hotel.reservationCode}</code></span>` : ''}
      <a href="${day.hotel.mapUrl}" target="_blank" rel="noreferrer">Konumu Aç ↗</a>
    </div>` : '';

  // Parking points
  const parkingHtml = day.parking?.length ? `
    <div class="day-parking-section">
      <small>🅿️ Önerilen Otopark Noktaları</small>
      <div class="parking-chips">
        ${day.parking.map(p => `
          <a class="parking-chip" href="${p.mapUrl}" target="_blank" rel="noreferrer" title="${p.description || ''}">
            <span>${p.type || 'Otopark'}:</span> ${p.title} ↗
          </a>`).join('')}
      </div>
    </div>` : '';

  // Recommended Fuel and Rest Stops
  const fuelStopsHtml = day.recommendedFuelAndRestStops?.length ? `
    <div class="day-fuel-section">
      <small>⛽ Günün Güvenli Otoyol Dinlenme (ΣΕΑ) ve Yakıt İstasyonları</small>
      <div class="fuel-chips">
        ${day.recommendedFuelAndRestStops.map(s => `
          <a class="fuel-chip" href="${s.MapUrl || mapsSearch(s.Name)}" target="_blank" rel="noreferrer" title="${s.Description}">
            <div class="fuel-chip-header">
              <strong>${s.Name}</strong>
              <span>${s.Highway} ↗</span>
            </div>
            <p>${s.Description}</p>
            <div class="fuel-tags">
              ${(s.Features || []).map(f => `<span>✓ ${f}</span>`).join('')}
            </div>
          </a>`).join('')}
      </div>
    </div>` : '';

  // Husband Non-Celiac Local Food Recommendations
  const husbandFoodHtml = day.husbandLocalFoodRecommendations?.length ? `
    <div class="day-husband-food">
      <div class="husband-food-header">
        <span class="husband-food-badge">🍴 Eş İçin Yerel Lezzet Durakları (Domuzsuz)</span>
        <small>Glutensiz diyet kısıtlaması olmayan eşin şehirdeki otantik lezzet tadımları</small>
      </div>
      <ul class="husband-food-list">
        ${day.husbandLocalFoodRecommendations.map(item => `<li>${item}</li>`).join('')}
      </ul>
    </div>` : '';

  const times = day.timeBlocks.map(block => `
    <div class="timeline-row">
      <div class="timeline-time">${block.startTime}${block.endTime ? ` — ${block.endTime}` : ''}</div>
      <div class="timeline-track"></div>
      <div>
        <div class="timeline-activity">${block.activity}</div>
        ${block.historyInfo ? `
          <div class="block-history">
            <strong>📜 Tarihi & Kültürel Bilgi:</strong>
            ${block.historyInfo}
          </div>` : ''}
        ${block.googleReviewNote ? `
          <div class="timeline-google-review">
            <strong>⭐ Google Yorumları & Pratik İpuçları:</strong>
            ${block.googleReviewNote}
          </div>` : ''}
      </div>
    </div>`).join('');

  $('#dayDetail').innerHTML = `
    <article class="day-panel" role="tabpanel">
      <div class="day-summary">
        <span class="day-date">${day.weekday} · ${formatDate(day.date)} · ${day.day}. gün</span>
        <h3>${day.title}</h3>
        
        ${alertHtml}
        ${hotelHtml}

        <div class="day-meta">
          <div><small>Rota</small><strong>${day.start} → ${day.end}</strong></div>
          <div><small>Konaklama</small><strong>${overnight}</strong></div>
          <div><small>Mesafe</small><strong>${distance(day.estimatedDistanceKm)}</strong></div>
          <div><small>Sürüş</small><strong>${driveTime(day)}</strong></div>
        </div>

        ${parkingHtml}
        ${fuelStopsHtml}
        ${husbandFoodHtml}

        ${day.attractions ? `<ul class="attractions">${day.attractions.map(item => `
          <li><a href="${mapsSearch(item)}" target="_blank" rel="noreferrer" aria-label="${item} konumunu Google Maps'te aç">${item}<span aria-hidden="true">↗</span></a></li>`).join('')}</ul>` : ''}

        ${day.optionalActivities?.length ? `
          <div class="optional-activities"><small>İsteğe bağlı</small><ul>${day.optionalActivities.map(item => `<li>${item}</li>`).join('')}</ul></div>` : ''}

        ${day.roadSequence ? `
          <div class="road-sequence"><small>Sürüş rotası</small><div>${day.roadSequence.map((stop, stopIndex) => `
            <a href="${mapsSearch(stop)}" target="_blank" rel="noreferrer">${stop}</a>${stopIndex < day.roadSequence.length - 1 ? '<span aria-hidden="true">→</span>' : ''}`).join('')}</div></div>` : ''}

        <a class="day-map" href="${day.mapUrl}" target="_blank" rel="noreferrer">Bu günü haritada aç ↗</a>
      </div>

      <div class="timeline">
        ${times}
        ${day.routeNotes?.length ? `
          <div class="day-notes">
            <strong>Yol ve Sürüş Notları</strong>
            <ul>${day.routeNotes.map(note => `<li>${note}</li>`).join('')}</ul>
          </div>` : ''}
      </div>

      <div class="day-extras">
        <details class="day-extra">
          <summary><span>🍴 Günün yemek planı</span><small>${day.mealPlan.length} öğün · ayrıntıları aç</small></summary>
          <div class="meal-list">${day.mealPlan.map(renderMeal).join('')}</div>
        </details>
        <details class="day-extra">
          <summary><span>€ Günlük ödeme planı</span><small>${day.dailyPaymentNotes.currenciesNeeded.join(' · ')}</small></summary>
          ${renderDailyPayments(day.dailyPaymentNotes)}
        </details>
      </div>
    </article>`;
}

function checklist(items, category) {
  if (!items?.length) return '';
  return `<div class="check-grid">${items.map((item, index) => {
    const key = `${currentTourKey}-${category}-${index}`;
    const checked = localStorage.getItem(key) === '1';
    return `<label class="check-item"><input type="checkbox" data-key="${key}" ${checked ? 'checked' : ''}><span class="fake-check">✓</span><span>${item}</span></label>`;
  }).join('')}</div>`;
}

function guideHeading(title, description) {
  return `<div class="guide-subheading"><h3>${title}</h3>${description ? `<p>${description}</p>` : ''}</div>`;
}

function renderGuide(type = 'summary') {
  let html = '';
  const summary = trip.tripSummary;
  const car = trip.rentalCarRequirements || trip.vehicleRequirements;

  if (type === 'summary') {
    const arrival = summary.arrival;
    const departure = summary.departure;
    html = `
      ${guideHeading('Plan ve Ulaşım Özeti', 'Temel seyahat, güzergah, otoyollar ve sürüş stratejisi.')}
      <div class="info-grid">
        <article class="info-card">
          <small>Plan Versiyonu</small>
          <h4>Versiyon ${trip.metadata.version}</h4>
          <p>${trip.metadata.title}</p>
          <p><b>Durum:</b> ${trip.metadata.planStatus}</p>
          <p><b>Güncelleme:</b> ${trip.metadata.updatedAt}</p>
          <p><b>Dil / Saat:</b> ${trip.metadata.language} · ${trip.metadata.timezone}</p>
        </article>
        <article class="info-card">
          <small>Yolcular ve Rota</small>
          <h4>${summary.travelers} kişi · ${summary.durationDays} gün</h4>
          <p>${summary.countries.join(' · ')}</p>
          <p><b>Rota Türü:</b> ${summary.vehicleType || 'Şahsi Araç (İlk Yurt Dışı Sürüşü)'}</p>
          <p><b>Sürüş:</b> ${summary.estimatedTotalDrivingHoursIncludingNormalBorders.min}–${summary.estimatedTotalDrivingHoursIncludingNormalBorders.max} saat</p>
          <p><b>Mesafe:</b> ${distance(summary.estimatedTotalDistanceKm)}</p>
        </article>
        <article class="info-card">
          <small>Gidiş / Gece Çıkış</small>
          <h4>${arrival.borderName || 'İpsala / Kipi'}</h4>
          <p><b>İstanbul Çıkış:</b> ${arrival.departureFromIstanbul || '23 Ekim 2026 22:00'}</p>
          <p><b>Sınır Geçiş:</b> ${arrival.estimatedBorderCrossingTime || '01:00 - 02:00'}</p>
          <p>${arrival.country} · ${arrival.note || ''}</p>
        </article>
        <article class="info-card">
          <small>Dönüş / Çıkış</small>
          <h4>${departure.borderName || 'Kipi / İpsala'} → ${departure.destination}</h4>
          <p>${formatDate(departure.date)}</p>
          <p>${departure.note || ''}</p>
        </article>
      </div>
      <div class="notice">
        <b>Onaylı Rota</b>
        <p>${trip.approvedRoute.routeText}</p>
        ${externalLink(trip.approvedRoute.googleMapsUrl, 'Rotayı Google Maps’te aç')}
      </div>`;
  }

  if (type === 'sos') {
    const sos = trip.greekSosCard;
    if (sos) {
      html = `
        <div class="guide-sos-container">
          ${guideHeading('Restoranlarda Garsona Gösterilecek Yunanca Çölyak & Helal Kartı', sos.description)}
          <div class="greek-display-card">
            <div class="greek-display-header">
              <h3>🇬🇷 ΠΡΟΣΟΧΗ: ΑΥΣΤΗΡΗ ΔΙΑΤΡΟΦΙΚΗ ΟΔΗΓΙΑ</h3>
              <button class="btn-copy-greek" id="copyGuideGreekBtn" type="button">📋 Yunanca Metni Kopyala</button>
            </div>
            <p class="greek-raw-text">${sos.greekText.replace(/\n\n/g, '<br><br>')}</p>
            <div class="tr-quote"><strong>Türkçe Çevirisi:</strong> ${sos.turkishTranslation}</div>
          </div>
          <div class="sos-guide-grid">
            <div class="sos-guide-box safe">
              <h4>✅ Doğal Glutensiz & Güvenli Seçenekler</h4>
              <ul>${sos.safeFoods.map(f => `<li><strong>${f.name}:</strong> ${f.desc}</li>`).join('')}</ul>
            </div>
            <div class="sos-guide-box warning">
              <h4>⚠️ Kaçınılması Gereken Gizli Tuzaklar</h4>
              <ul>${sos.hiddenTraps.map(t => `<li><strong>${t.name}:</strong> ${t.desc}</li>`).join('')}</ul>
            </div>
          </div>
        </div>`;
    }
  }

  if (type === 'documents') {
    html = `${guideHeading('Belge Kontrolü', 'Sınır geçişleri ve araç işlemleri için yanınızda bulunması gereken evraklar.')}${checklist(trip.documentsChecklist, 'documents')}`;
  }

  if (type === 'car') {
    if (car.checksBeforeDeparture) {
      // Kişisel Araç (Yunanistan)
      html = `
        ${guideHeading('Şahsi Araçla Yurt Dışı Sürüş Planı', 'İstanbul çıkışlı güvenli otoyol güzergahı ve sınır hazırlıkları.')}
        <div class="info-grid car-facts">
          <article class="info-card"><small>Araç Türü</small><h4>${car.vehicleType}</h4><p>Çıkış ve Dönüş: İstanbul</p></article>
          <article class="info-card"><small>Ana Otoyollar</small><h4>A2 (Egnatia Odos) & A1</h4><p>Bölünmüş ücretli otoyol ağı</p></article>
          <article class="info-card"><small>Gerekli Sigorta</small><h4>Yeşilkart Sigortası (Green Card)</h4><p>Torpido gözünde hazır bulundurulmalıdır</p></article>
        </div>
        <div class="notice warning"><b>Önemli Prensip</b><p>${car.importantNote}</p></div>
        ${guideHeading('Yola Çıkmadan Önce', 'Araç ve belgeler için tamamlanacak kontroller.')}${checklist(car.checksBeforeDeparture, 'car-checks')}
        ${guideHeading('Sınır Kapısı Kontrolleri', 'Gümrük sahasına girerken hazır edilecekler.')}${checklist(car.borderInspectionChecklist, 'border-checks')}`;
    } else {
      // Kiralık Araç (Balkanlar)
      html = `
        ${guideHeading('Kiralık Araç Planı', `${car.pickupLocation} noktasından teslim alınıp aynı noktaya bırakılacak.`)}
        <div class="info-grid car-facts">
          <article class="info-card"><small>Teslim Alma</small><h4>${new Date(car.pickupPlannedAt).toLocaleString('tr-TR', { dateStyle: 'long', timeStyle: 'short' })}</h4><p>${car.pickupLocation}</p></article>
          <article class="info-card"><small>Son Teslim</small><h4>${new Date(car.returnDeadline).toLocaleString('tr-TR', { dateStyle: 'long', timeStyle: 'short' })}</h4><p>${car.returnLocation}</p></article>
          <article class="info-card"><small>Sınır İzni Gereken Ülkeler</small><h4>${car.requiredCrossBorderCountries.join(' · ')}</h4></article>
        </div>
        <div class="notice warning"><b>Önemli</b><p>${car.importantNote}</p></div>
        ${guideHeading('Rezervasyondan Önce', 'Firma ile yazılı olarak doğrulanacak maddeler.')}${checklist(car.checksBeforeBooking, 'car-booking')}
        ${guideHeading('Aracı Teslim Alırken', 'Teslim alanında tamamlanacak kontroller.')}${checklist(car.pickupInspectionChecklist, 'car-pickup')}`;
    }
  }

  if (type === 'stay') {
    html = `${guideHeading('Konaklama Planı', 'Tüm oteller rezerve edilmiş olup otopark ve merkezi erişim avantajı sunmaktadır.')}
      <div class="stay-grid">${trip.accommodationPlan.map(stay => {
        const rev = stay.googleReviewsSummary;
        return `
        <article class="stay-card">
          <small>${formatDate(stay.checkIn)} → ${formatDate(stay.checkOut)} · ${stay.nights} gece</small>
          <h3>${stay.hotelName || stay.city}</h3>
          ${stay.reservationCode ? `<p><b>Rezervasyon Kodu:</b> <code>${stay.reservationCode}</code></p>` : ''}
          <p><strong>Bölge:</strong> ${stay.recommendedAreas.join(', ')}</p>
          <p><strong>Öncelik:</strong> ${stay.requirements.join(' · ')}</p>
          ${stay.avoid?.length ? `<p class="avoid"><strong>Kaçının:</strong> ${stay.avoid.join(' · ')}</p>` : ''}
          ${rev ? `
            <div class="stay-reviews">
              <div class="stay-rating-row">
                <span class="stay-rating-badge">⭐ Google: ${rev.googleRating}</span>
              </div>
              <p class="stay-highlights">${rev.highlights}</p>
              ${rev.warningsAndTips?.length ? `
                <ul class="stay-tips-list">
                  ${rev.warningsAndTips.map(t => `<li>${t}</li>`).join('')}
                </ul>` : ''}
            </div>` : ''}
          ${stay.mapUrl ? `<p style="margin-top:12px;"><a class="inline-link" href="${stay.mapUrl}" target="_blank" rel="noreferrer">Haritada Aç ↗</a></p>` : ''}
        </article>`;
      }).join('')}</div>`;
  }

  if (type === 'food') {
    const food = trip.foodGuide;
    const pref = food.preferencesToConfirm;
    const nonCeliac = food.localDelicaciesForNonCeliacTraveler;
    html = `${guideHeading('Yeme–İçme & Çölyak Rehberi', 'Özel diyet gereksinimleri, güvenli sipariş kuralları ve Yunanca pratik ifadeler.')}
      <div class="preference-grid">
        <div><small>Domuz Eti Kısıtlaması</small><strong>${yesNo(pref.porkAllowed)} · ${pref.porkRestriction}</strong><p>${pref.porkRestrictionNote}</p></div>
        <div><small>Çölyak & Glütensiz Zorunluluk</small><strong>${pref.celiacDiseaseStrict ? 'Kesin (%100)' : 'Normal'}</strong><p>${pref.celiacDiseaseNote || 'Çapraz bulaşma kesinlikle önlenmelidir.'}</p></div>
        <div><small>Deniz Ürünü Tercihi</small><strong>${yesNo(pref.seafoodPreferred)}</strong><p>${pref.seafoodPreferenceNote}</p></div>
        <div><small>Kişi Başı Hedef Bütçe</small><strong>${pref.targetMealBudgetPerPerson || 'Esnek'}</strong><p>${pref.budgetPolicy}</p></div>
      </div>
      
      ${food.certifiedBakeries?.length ? `
        ${guideHeading('Glütensiz Sertifikalı Fırınlar')}
        <div class="info-grid">
          ${food.certifiedBakeries.map(b => `
            <article class="info-card">
              <small>${b.city}</small>
              <h4>${b.name}</h4>
              <p><b>Çalışma:</b> ${b.workingHours}</p>
              <p><b>Öne Çıkanlar:</b> ${b.specialties}</p>
              ${externalLink(b.mapUrl, 'Fırın Konumunu Aç')}
            </article>`).join('')}
        </div>` : ''}

      ${nonCeliac ? `
        ${guideHeading(nonCeliac.title || 'Eş İçin Yöresel Lezzet Durakları (Domuzsuz)', nonCeliac.importantRule)}
        <div class="must-try-grid">
          ${(nonCeliac.mustTryItems || []).map(item => `
            <article class="must-try-card">
              <span class="must-try-city">${item.city}</span>
              <h4>${item.name}</h4>
              <p class="must-try-desc">${item.types}</p>
              ${item.warning ? `<div class="must-try-warn">⚠️ <strong>Tüketim İpucu:</strong> ${item.warning}</div>` : ''}
            </article>`).join('')}
        </div>` : ''}

      ${guideHeading('Yemek Siparişinde İşe Yarayan İfadeler')}
      <div class="phrase-grid">${food.usefulDietaryPhrases.map(item => `
        <article><small>${item.language}</small><strong>${item.phrase}</strong><p>${item.meaning}</p></article>`).join('')}</div>

      ${guideHeading('Sipariş Notları')}${list(food.generalOrderingNotes, 'guide-list')}
      <div class="notice warning"><b>Doğrulama Notu</b><p>${food.finalVerificationWindow}</p></div>`;
  }

  if (type === 'stations') {
    const stationsData = trip.highwayRestStationsAndFuelStops;
    if (stationsData) {
      html = `
        ${guideHeading(stationsData.title, 'Yunanistan A2 (Egnatia Odos) ve A1 otoyolları üzerinde 24 saat açık, aydınlatmalı, kameralı ve marketli resmi otoyol dinlenme tesisleri.')}
        <div class="notice warning">
          <b>Kritik Güvenlik Kuralı</b>
          <p>${stationsData.criticalRule}</p>
        </div>
        <div class="stations-grid">
          ${stationsData.stations.map(st => `
            <article class="station-card">
              <div class="station-card-top">
                <span class="station-order">${st.Order}</span>
                <div class="station-card-title">
                  <h4>${st.Name}</h4>
                  <span class="station-highway">${st.Highway}</span>
                </div>
              </div>
              <div class="station-route">📍 ${st.RouteSegment}</div>
              <p class="station-desc">${st.Description}</p>
              <div class="station-features">
                ${st.Features.map(f => `<span>✓ ${f}</span>`).join('')}
              </div>
              <a class="station-map-btn" href="${st.MapUrl || mapsSearch(st.Name)}" target="_blank" rel="noreferrer">Google Maps'te Aç ↗</a>
            </article>`).join('')}
        </div>`;
    }
  }

  if (type === 'money') {
    const money = trip.moneyAndPayments;
    const reserve = money.cashStrategy.euroEmergencyReserveForTwo;
    html = `${guideHeading('Para Birimleri ve Ödeme', `Ana referans para birimi ${money.mainReferenceCurrency}. Kartın yanında otopark ve gişeler için nakit yedeği planlanıyor.`)}
      <div class="currency-grid">${trip.currencies.map(item => `
        <article class="currency-card">
          <div><small>${item.country}</small><strong>${item.code}</strong></div>
          <h4>${item.currency}</h4>
          <p>${item.cardAcceptance}</p>
          ${item.euroUsage ? `<p><b>Euro:</b> ${item.euroUsage}</p>` : ''}
          <p><b>Nakit Önerisi:</b> ${yesNo(item.cashRecommended)}</p>
          <div class="cash-band">
            <strong>${item.planningCashBandForTwo.min}–${item.planningCashBandForTwo.max} ${item.planningCashBandForTwo.currency}</strong>
            <span>${item.planningCashBandForTwo.scope}</span>
          </div>
        </article>`).join('')}</div>

      <div class="notice warning">
        <b>Acil Durum Nakit Rezervi: ${reserve.min}–${reserve.max} ${reserve.currency}</b>
        <p>${reserve.note}</p>
      </div>
      ${guideHeading('Nakit & Gişe Kuralları')}${list(money.cashStrategy.localCurrencyRules, 'guide-list')}
      ${guideHeading('Kart ve ATM Kontrolü')}${checklist(money.cardAndAtmChecklist, 'money-card')}
      ${guideHeading('Yol & Gişe Ödemeleri')}
      <div class="road-payment-grid">${money.roadPaymentPlan.map(item => `
        <article>
          <small>${statusLabel(item.verificationStatus)}</small>
          <h4>${item.country}</h4>
          <p><b>Olası Ödemeler:</b> ${item.possiblePayments.join(' · ')}</p>
          <p><b>Yedek:</b> ${item.recommendedPaymentBackup.join(' · ')}</p>
          ${item.note ? `<p>${item.note}</p>` : ''}
        </article>`).join('')}</div>`;
  }

  if (type === 'borders') {
    html = `${guideHeading('Sınır Geçişleri', 'Pasaport ve gümrük kontrolleri rehberi.')}
      <div class="border-grid">${trip.borderCrossings.map(item => `
        <article>
          <span>${item.sequence}</span>
          <div>
            <small>${formatDate(item.date)}</small>
            <h4>${item.fromCountry} → ${item.toCountry}</h4>
            <p>${item.crossingNames.join(' / ')}</p>
            ${item.notes ? `<p style="margin-top:6px; color:#64748b; font-size:10px;">${item.notes}</p>` : ''}
          </div>
        </article>`).join('')}</div>
      ${guideHeading('Navigasyon ve Güvenli Sürüş Notları')}${checklist(trip.navigationAndDrivingNotes, 'navigation')}`;
  }

  if (type === 'packing') {
    html = `${guideHeading('Valiz ve Pratik İhtiyaçlar', 'Araç, sınır, tapınak ve lagün günleri için hazırlık listesi.')}${checklist(trip.packingAndPracticalChecklist, 'packing')}`;
  }

  if (type === 'sources') {
    html = `${guideHeading('Kaynaklar', `${trip.sourceReferences.length} resmi ve güncel seyahat kaynağı.`)}
      <div class="source-grid">${trip.sourceReferences.map((source, index) => `
        <a href="${source.url}" target="_blank" rel="noreferrer">
          <span>${String(index + 1).padStart(2, '0')}</span>
          <div><strong>${source.title}</strong><p>${source.usedFor}</p></div>
          <b>↗</b>
        </a>`).join('')}</div>`;
  }

  $('#guideContent').innerHTML = html;
  
  // Attach guide copy button event if inside SOS tab
  const guideCopyBtn = $('#copyGuideGreekBtn');
  if (guideCopyBtn && trip.greekSosCard) {
    guideCopyBtn.onclick = () => copyTextToClipboard(trip.greekSosCard.greekText, guideCopyBtn);
  }

  $('#guideContent').querySelectorAll('input[data-key]').forEach(input => {
    input.addEventListener('change', () => localStorage.setItem(input.dataset.key, input.checked ? '1' : '0'));
  });
}

function copyTextToClipboard(text, btnElement) {
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btnElement.textContent;
    btnElement.textContent = '✓ Kopyalandı!';
    btnElement.classList.add('copied');
    setTimeout(() => {
      btnElement.textContent = originalText;
      btnElement.classList.remove('copied');
    }, 2500);
  }).catch(err => {
    console.error('Kopyalama hatası:', err);
    alert('Metin kopyalanamadı, lütfen ekrandan seçip kopyalayın.');
  });
}

function setupSosModal() {
  const modal = $('#sosModal');
  const openBtns = [$('#openSosBtn'), $('#heroSosBtn')].filter(Boolean);
  const closeBtn = $('#closeSosBtn');
  const copyBtn = $('#copyGreekBtn');

  openBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('open');
    });
  });
  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.remove('open');
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('open');
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      modal.classList.remove('open');
    }
  });

  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const text = trip?.greekSosCard?.greekText || $('#greekRawText')?.innerText || '';
      copyTextToClipboard(text, copyBtn);
    });
  }
}

function setupGuideTabs() {
  const container = $('#guideTabs');
  if (!container) return;
  const buttons = container.querySelectorAll('button[data-guide]');
  buttons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGuide(btn.dataset.guide);
    });
  });
}

function setupTourSwitcher() {
  const switcher = $('#tourSwitch');
  if (!switcher) return;

  switcher.onclick = (e) => {
    const btn = e.target.closest('[data-tour]');
    if (!btn || btn.classList.contains('active')) return;

    switcher.querySelectorAll('.tour-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentTourKey = btn.dataset.tour;
    loadTour(currentTourKey);
  };
}

async function loadTour(tourKey) {
  const loading = $('#loading');
  loading.classList.remove('hidden');
  try {
    const tourCfg = TOURS[tourKey];
    const response = await fetch(tourCfg.file);
    if (!response.ok) throw new Error(`Veri yüklenemedi (${response.status})`);
    trip = await response.json();

    renderSummary();
    renderRoute();
    renderDayTabs();

    // Default to summary or sos guide
    const activeGuideBtn = $('#guideTabs button.active');
    renderGuide(activeGuideBtn ? activeGuideBtn.dataset.guide : 'summary');
    $('#year').textContent = new Date().getFullYear();
  } catch (error) {
    loading.innerHTML = `<strong>Rota yüklenemedi</strong><small>${error.message}<br>Siteyi yerel bir web sunucusu üzerinden açmayı deneyin.</small>`;
    console.error(error);
    return;
  }
  loading.classList.add('hidden');
}

function init() {
  setupTourSwitcher();
  setupGuideTabs();
  setupSosModal();
  loadTour(currentTourKey);
}

init();
