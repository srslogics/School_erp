const CACHE_NAME = "octominds-erp-demo-v3";
const APP_SHELL = [
  "./",
  "./index.html",
  "./health.html",
  "./manifest.webmanifest",
  "./icon-192.svg",
  "./icon-512.svg",
  "./icon-192.png",
  "./icon-512.png"
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
  const url = new URL(request.url);
  const isSameOrigin = url.origin === self.location.origin;
  const isNavigation = request.mode === "navigate" || (request.headers.get("accept") || "").includes("text/html");

  if (!isSameOrigin) {
    return;
  }

  if (isNavigation) {
    event.respondWith(
      fetch(request, { cache: "no-store" })
        .then((networkResponse) => {
          const responseClone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put("./index.html", responseClone);
            cache.put(request, networkResponse.clone());
          });
          return networkResponse;
        })
        .catch(async () => {
          const cachedResponse = await caches.match(request);
          if (cachedResponse) return cachedResponse;
          return caches.match("./index.html");
        })
    );
    return;
  }

  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      const networkFetch = fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.ok) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, responseClone);
            });
          }
          return networkResponse;
        })

      if (cachedResponse) {
        return cachedResponse;
      }

      return networkFetch.catch(() => {
        if ((request.headers.get("accept") || "").includes("image/")) {
          return caches.match("./icon-192.png");
        }
        return caches.match("./index.html");
      });
    })
  );
});
