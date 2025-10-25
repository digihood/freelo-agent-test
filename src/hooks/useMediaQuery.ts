import { useState, useEffect } from 'react';

/**
 * Custom hook to detect viewport breakpoints using window.matchMedia
 * Returns current screen size category for responsive behavior
 */
export type ScreenSize = 'mobile' | 'tablet' | 'desktop';

interface MediaQueryBreakpoints {
  mobile: string;
  tablet: string;
  desktop: string;
}

const defaultBreakpoints: MediaQueryBreakpoints = {
  mobile: '(max-width: 767px)',
  tablet: '(min-width: 768px) and (max-width: 1023px)',
  desktop: '(min-width: 1024px)',
};

export const useMediaQuery = (breakpoints: MediaQueryBreakpoints = defaultBreakpoints): ScreenSize => {
  const [screenSize, setScreenSize] = useState<ScreenSize>(() => {
    if (typeof window === 'undefined') return 'desktop';

    if (window.matchMedia(breakpoints.mobile).matches) return 'mobile';
    if (window.matchMedia(breakpoints.tablet).matches) return 'tablet';
    return 'desktop';
  });

  useEffect(() => {
    const mobileQuery = window.matchMedia(breakpoints.mobile);
    const tabletQuery = window.matchMedia(breakpoints.tablet);
    const desktopQuery = window.matchMedia(breakpoints.desktop);

    const updateScreenSize = () => {
      if (mobileQuery.matches) setScreenSize('mobile');
      else if (tabletQuery.matches) setScreenSize('tablet');
      else if (desktopQuery.matches) setScreenSize('desktop');
    };

    mobileQuery.addEventListener('change', updateScreenSize);
    tabletQuery.addEventListener('change', updateScreenSize);
    desktopQuery.addEventListener('change', updateScreenSize);

    return () => {
      mobileQuery.removeEventListener('change', updateScreenSize);
      tabletQuery.removeEventListener('change', updateScreenSize);
      desktopQuery.removeEventListener('change', updateScreenSize);
    };
  }, [breakpoints]);

  return screenSize;
};
