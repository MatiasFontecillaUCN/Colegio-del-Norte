import { writable } from 'svelte/store';

const createAuthStore = () => {
  const { subscribe, set } = writable({ token: null });

  return {
    subscribe,
    setToken: (token) => {
        sessionStorage.setItem('jwtToken', token);
        set({ token });
    },
    clearToken: () => {
        sessionStorage.removeItem('jwtToken');
        set({ token: null });
    },
  };
};

export const auth = createAuthStore();
