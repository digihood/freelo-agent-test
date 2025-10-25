import React from 'react';

interface HamburgerIconProps {
  isOpen: boolean;
  onClick: () => void;
  ariaLabel?: string;
}

/**
 * Animated hamburger menu icon component
 * Displays three horizontal lines that transform into an X when open
 */
export const HamburgerIcon: React.FC<HamburgerIconProps> = ({
  isOpen,
  onClick,
  ariaLabel = 'Toggle navigation menu',
}) => {
  return (
    <button
      className={`hamburger-icon ${isOpen ? 'open' : ''}`}
      onClick={onClick}
      aria-label={ariaLabel}
      aria-expanded={isOpen}
      type="button"
    >
      <span className="hamburger-line hamburger-line-top"></span>
      <span className="hamburger-line hamburger-line-middle"></span>
      <span className="hamburger-line hamburger-line-bottom"></span>
    </button>
  );
};
