const CACHE_NAME = "octominds-erp-demo-v1";
const APP_SHELL = [
  "/octominds-preschool-demo/",
  "/octominds-preschool-demo/index.html",
  "/octominds-preschool-demo/manifest.webmanifest",
  "/octominds-preschool-demo/icon-192.svg",
  "/octominds-preschool-demo/icon-512.svg",
  "/assets/css/main.css",
  "/assets/js/site-nav.js",
  "/assets/images/favicon-192.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(APP_SHELL))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((key) => key !== CACHE_NAME)
          .map((key) => caches.delete(key))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      if (cachedResponse) return cachedResponse;

      return fetch(request)
        .then((networkResponse) => {
          const responseClone = networkResponse.clone();
          if (request.url.startsWith(self.location.origin)) {
            caches.open(CACHE_NAME).then((cache) => cache.put(request, responseClone));
          }
          return networkResponse;
        })
        .catch(() => caches.match("/octominds-preschool-demo/index.html"));
    })
  );
});
